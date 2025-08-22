import urequests as requests
import ujson as json
import time
from .models import ChatMessage, ChatResponse, ModelConfig
from .utils import format_prompt, validate_response

class AIClient:
    """
    Main client class for interacting with AI/LLM APIs
    """
    
    def __init__(self, api_key=None, base_url=None, model_config=None):
        self.api_key = api_key
        self.base_url = base_url or "https://api.openai.com/v1"
        self.model_config = model_config or ModelConfig()
        self.session_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}" if self.api_key else None
        }
    
    def chat_completion(self, messages, stream=False):
        """
        Send a chat completion request to the AI API
        
        Args:
            messages: List of ChatMessage objects or dict messages
            stream: Whether to stream the response (default: False)
            
        Returns:
            ChatResponse object
        """
        try:
            # Format messages
            formatted_messages = []
            for msg in messages:
                if isinstance(msg, ChatMessage):
                    formatted_messages.append(msg.to_dict())
                else:
                    formatted_messages.append(msg)
            
            # Prepare request payload
            payload = {
                "model": self.model_config.model_name,
                "messages": formatted_messages,
                "max_tokens": self.model_config.max_tokens,
                "temperature": self.model_config.temperature,
                "stream": stream
            }
            
            # Make request
            url = f"{self.base_url}/chat/completions"
            response = requests.post(
                url,
                headers=self.session_headers,
                data=json.dumps(payload)
            )
            
            if response.status_code == 200:
                response_data = response.json()
                return ChatResponse.from_api_response(response_data)
            else:
                raise Exception(f"API Error: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"Error in chat_completion: {e}")
            return None
        finally:
            if 'response' in locals():
                response.close()
    
    def simple_chat(self, prompt, system_message=None):
        """
        Simple chat interface for single prompts
        
        Args:
            prompt: User prompt string
            system_message: Optional system message
            
        Returns:
            String response or None if error
        """
        messages = []
        
        if system_message:
            messages.append(ChatMessage("system", system_message))
        
        messages.append(ChatMessage("user", prompt))
        
        response = self.chat_completion(messages)
        
        if response and response.choices:
            return response.choices[0].message.content
        return None
    
    def set_model_config(self, model_config):
        """
        Update model configuration
        """
        self.model_config = model_config
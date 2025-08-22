from ..client import AIClient
from ..models import ChatMessage, ModelConfig
from ..utils import format_prompt, validate_response

class BaseAIApplication:
    """
    Base class for AI-powered applications with predefined prompts
    """
    
    def __init__(self, ai_client, system_prompt=None, temperature=0.7):
        self.ai_client = ai_client
        self.system_prompt = system_prompt or self.get_default_system_prompt()
        self.conversation_history = []
        self.temperature = temperature
        
        # Update client temperature
        if hasattr(self.ai_client, 'model_config'):
            self.ai_client.model_config.temperature = temperature
    
    def get_default_system_prompt(self):
        """
        Override this method in subclasses to provide default system prompt
        """
        return "You are a helpful AI assistant."
    
    def process_query(self, user_input, context_data=None):
        """
        Process user query with optional context data
        
        Args:
            user_input: User's question or command
            context_data: Additional context (sensor data, device status, etc.)
            
        Returns:
            AI response string
        """
        # Format the prompt with context if provided
        formatted_prompt = self.format_user_prompt(user_input, context_data)
        
        # Create messages
        messages = [ChatMessage("system", self.system_prompt)]
        
        # Add conversation history (last 5 exchanges to manage memory)
        messages.extend(self.conversation_history[-10:])
        
        # Add current user message
        messages.append(ChatMessage("user", formatted_prompt))
        
        # Get AI response
        response = self.ai_client.chat_completion(messages)
        
        if response and response.choices:
            ai_response = response.choices[0].message.content
            
            # Update conversation history
            self.conversation_history.append(ChatMessage("user", formatted_prompt))
            self.conversation_history.append(ChatMessage("assistant", ai_response))
            
            return validate_response(ai_response)
        
        return None
    
    def format_user_prompt(self, user_input, context_data=None):
        """
        Format user prompt with context data
        Override in subclasses for specific formatting
        """
        if context_data:
            return f"User Query: {user_input}\n\nContext Data: {context_data}"
        return user_input
    
    def clear_history(self):
        """
        Clear conversation history
        """
        self.conversation_history = []
    
    def set_system_prompt(self, new_prompt):
        """
        Update system prompt
        """
        self.system_prompt = new_prompt
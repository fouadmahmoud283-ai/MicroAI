# Basic chat example using the AI/LLM library

import sys
sys.path.append('/lib')

from ai_llm import AIClient, ModelConfig

# Configuration
API_KEY = "your-api-key-here"
BASE_URL = "https://api.openai.com/v1"  # or your preferred API endpoint

def main():
    # Initialize client
    config = ModelConfig(
        model_name="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.7
    )
    
    client = AIClient(
        api_key=API_KEY,
        base_url=BASE_URL,
        model_config=config
    )
    
    # Simple chat
    response = client.simple_chat(
        prompt="Hello! Can you help me with MicroPython?",
        system_message="You are a helpful MicroPython assistant."
    )
    
    if response:
        print("AI Response:", response)
    else:
        print("Failed to get response")

if __name__ == "__main__":
    main()
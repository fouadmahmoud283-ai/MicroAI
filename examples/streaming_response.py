# Streaming response example (basic implementation)

import sys
sys.path.append('/lib')

from ai_llm import AIClient, ChatMessage, ModelConfig

def main():
    client = AIClient(
        api_key="your-api-key-here",
        model_config=ModelConfig(model_name="gpt-3.5-turbo")
    )
    
    messages = [
        ChatMessage("system", "You are a helpful assistant."),
        ChatMessage("user", "Explain MicroPython in simple terms.")
    ]
    
    # Note: Streaming implementation would require additional handling
    response = client.chat_completion(messages, stream=False)
    
    if response and response.choices:
        print("Response:", response.choices[0].message.content)

if __name__ == "__main__":
    main()
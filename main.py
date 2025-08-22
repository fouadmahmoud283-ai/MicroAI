# Main application file
# This demonstrates basic usage of the AI/LLM library

import sys
sys.path.append('/lib')

from ai_llm import AIClient, ModelConfig
import time

def setup_wifi():
    """
    Setup WiFi connection (customize for your network)
    """
    import network
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect('YOUR_SSID', 'YOUR_PASSWORD')
        
        while not wlan.isconnected():
            time.sleep(1)
            print('.', end='')
    
    print('\nWiFi connected:', wlan.ifconfig())

def main():
    # Setup WiFi
    setup_wifi()
    
    # Initialize AI client
    config = ModelConfig(
        model_name="gpt-3.5-turbo",
        max_tokens=150,
        temperature=0.7
    )
    
    client = AIClient(
        api_key="your-api-key-here",
        base_url="https://api.openai.com/v1",
        model_config=config
    )
    
    # Test the library
    print("Testing AI/LLM Library...")
    
    response = client.simple_chat(
        "What is MicroPython?",
        "You are a helpful programming assistant."
    )
    
    if response:
        print("AI Response:", response)
    else:
        print("Failed to get response from AI")

if __name__ == "__main__":
    main()
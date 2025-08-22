import sys
sys.path.append('/lib')

from ai_llm import AIClient, ModelConfig, SmartHomeController
import ujson as json

def main():
    # Setup AI client
    client = AIClient(
        api_key="your-api-key-here",
        model_config=ModelConfig(model_name="gpt-3.5-turbo")
    )
    
    # Create smart home controller
    home_ai = SmartHomeController(
        ai_client=client,
        home_config={
            "rooms": ["living_room", "bedroom", "kitchen"],
            "devices": {
                "lights": ["main_lights", "accent_lights"],
                "climate": ["thermostat", "ceiling_fan"],
                "appliances": ["tv", "coffee_maker"]
            }
        }
    )
    
    # Sample home status
    home_status = {
        "living_room": {
            "main_lights": {"on": True, "brightness": 75},
            "tv": {"on": False},
            "temperature": 22.5
        },
        "bedroom": {
            "main_lights": {"on": False},
            "temperature": 20.0
        }
    }
    
    # Test commands
    commands = [
        "Turn on the bedroom lights at 50% brightness",
        "Set the living room temperature to 24 degrees",
        "Create a movie night scene",
        "Turn off all lights in 30 minutes"
    ]
    
    for command in commands:
        print(f"\n=== Command: {command} ===")
        result = home_ai.process_home_command(command, home_status)
        
        if result:
            print(json.dumps(result, indent=2))
        else:
            print("Failed to process command")

if __name__ == "__main__":
    main()
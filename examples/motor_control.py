import sys
sys.path.append('/lib')

from ai_llm import AIClient, ModelConfig, MotorController
import ujson as json

def main():
    # Setup AI client
    client = AIClient(
        api_key="your-api-key-here",
        model_config=ModelConfig(model_name="gpt-3.5-turbo")
    )
    
    # Create motor controller
    motor_ai = MotorController(
        ai_client=client,
        motor_config={
            "max_speed": 100,
            "min_speed": 0,
            "max_angle": 180,
            "min_angle": 0,
            "motor_types": ["servo", "stepper"]
        }
    )
    
    # Current motor status
    motor_status = {
        "servo_1": {"running": False, "angle": 90, "speed": 0},
        "stepper_1": {"running": True, "speed": 25, "temperature": 45}
    }
    
    # Test commands
    commands = [
        "Turn servo_1 to 45 degrees slowly",
        "Stop all motors",
        "Rotate stepper_1 clockwise at 75% speed for 5 seconds",
        "Move servo_1 to home position"
    ]
    
    for command in commands:
        print(f"\n=== Command: {command} ===")
        result = motor_ai.process_motor_command(command, motor_status)
        
        if result:
            print(json.dumps(result, indent=2))
            
            # Execute command (this would interface with actual motor drivers)
            if result.get("safety_check") == "passed":
                print("✅ Command is safe to execute")
            elif result.get("safety_check") == "warning":
                print("⚠️ Command has warnings:", result.get("warnings"))
            else:
                print("❌ Command failed safety check")
        else:
            print("Failed to process command")

if __name__ == "__main__":
    main()
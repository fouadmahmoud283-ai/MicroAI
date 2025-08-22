import sys
sys.path.append('/lib')

from ai_llm import AIClient, ModelConfig, RobotNavigator, TaskScheduler
import ujson as json

def main():
    # Setup AI client
    client = AIClient(
        api_key="your-api-key-here",
        model_config=ModelConfig(model_name="gpt-3.5-turbo")
    )
    
    # Create robot navigator
    robot_nav = RobotNavigator(
        ai_client=client,
        robot_config={
            "robot_type": "cleaning_robot",
            "sensors": ["ultrasonic", "camera", "lidar"],
            "max_speed": 0.5
        }
    )
    
    # Create task scheduler
    task_scheduler = TaskScheduler(
        ai_client=client,
        scheduler_config={
            "task_types": ["cleaning", "patrol", "maintenance"]
        }
    )
    
    # Sample sensor data
    sensor_data = {
        "ultrasonic": {"front": 1.2, "left": 0.8, "right": 2.0},
        "camera": {"objects_detected": 2, "path_clear": True},
        "lidar": {"obstacles": [[1.0, 0.5], [2.0, -0.3]]}
    }
    
    current_position = {"x": 0.0, "y": 0.0, "theta": 0.0}
    
    # Navigation commands
    nav_commands = [
        "Move forward 2 meters",
        "Turn left and avoid the obstacle",
        "Go to the kitchen and clean the floor",
        "Return to charging station"
    ]
    
    print("=== Robot Navigation Demo ===")
    for command in nav_commands:
        print(f"\nCommand: {command}")
        result = robot_nav.process_navigation_command(command, sensor_data, current_position)
        
        if result:
            print(json.dumps(result, indent=2))
    
    # Task scheduling
    print("\n=== Task Scheduling Demo ===")
    schedule_request = "Schedule daily cleaning routine for the house, prioritizing high-traffic areas"
    
    system_status = {
        "battery": {"level": 85, "charging": False},
        "sensors": {"status": "operational"},
        "motors": {"status": "ready"}
    }
    
    schedule_result = task_scheduler.create_task_schedule(schedule_request, system_status)
    
    if schedule_result:
        print(json.dumps(schedule_result, indent=2))

if __name__ == "__main__":
    main()
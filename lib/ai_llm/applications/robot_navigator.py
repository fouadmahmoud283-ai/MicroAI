from .base_application import BaseAIApplication
import ujson as json

class RobotNavigator(BaseAIApplication):
    """
    AI-powered robot navigation and path planning system
    """
    
    def __init__(self, ai_client, robot_config=None):
        self.robot_config = robot_config or {
            "robot_type": "mobile_robot",
            "sensors": ["ultrasonic", "camera", "lidar", "imu", "encoders"],
            "capabilities": ["navigation", "obstacle_avoidance", "mapping", "localization"],
            "max_speed": 1.0,  # m/s
            "turning_radius": 0.3,  # meters
            "safety_distance": 0.2  # meters
        }
        super().__init__(ai_client, temperature=0.2)
    
    def get_default_system_prompt(self):
        return f"""
You are an expert robot navigation AI responsible for:

1. Planning safe and efficient paths for robot movement
2. Processing sensor data for obstacle detection and avoidance
3. Interpreting natural language navigation commands
4. Optimizing routes based on robot capabilities and constraints
5. Providing real-time navigation decisions
6. Managing simultaneous localization and mapping (SLAM)

Robot Configuration:
- Type: {self.robot_config['robot_type']}
- Sensors: {', '.join(self.robot_config['sensors'])}
- Max Speed: {self.robot_config['max_speed']} m/s
- Turning Radius: {self.robot_config['turning_radius']} m
- Safety Distance: {self.robot_config['safety_distance']} m

RESPONSE FORMAT:
Always respond with a JSON object containing:
{{
    "action": "move/turn/stop/scan/map",
    "direction": "forward/backward/left/right/custom_angle",
    "parameters": {{
        "speed": "0.0-{self.robot_config['max_speed']}_ms",
        "distance": "meters_to_travel",
        "angle": "degrees_to_turn",
        "duration": "seconds"
    }},
    "path_points": [["x1,y1"], ["x2,y2"]],
    "obstacles_detected": [["obstacle_positions"]],
    "confidence": "0-100_percent",
    "safety_status": "safe/caution/danger",
    "alternative_routes": ["backup_navigation_options"],
    "explanation": "reasoning_for_navigation_decision"
}}

Prioritize safety and collision avoidance in all navigation decisions.
"""
    
    def process_navigation_command(self, user_command, sensor_data=None, current_position=None):
        """
        Process natural language navigation commands
        
        Args:
            user_command: Natural language navigation instruction
            sensor_data: Current sensor readings
            current_position: Robot's current position and orientation
            
        Returns:
            Navigation command with path planning
        """
        context = self.format_navigation_context(sensor_data, current_position)
        response = self.process_query(user_command, context)
        
        if response:
            try:
                nav_command = json.loads(response)
                return self.validate_navigation_command(nav_command)
            except:
                return {
                    "action": "stop",
                    "safety_status": "danger",
                    "explanation": "Navigation command parsing failed - stopping for safety",
                    "raw_response": response
                }
        return None
    
    def format_navigation_context(self, sensor_data, current_position):
        """
        Format sensor data and position for navigation context
        """
        context_lines = []
        
        if current_position:
            context_lines.append(f"Current Position: {json.dumps(current_position)}")
        
        if sensor_data:
            context_lines.append("Sensor Data:")
            for sensor, data in sensor_data.items():
                if isinstance(data, dict):
                    sensor_info = f"  {sensor}: "
                    details = []
                    
                    if 'distance' in data:
                        details.append(f"Distance: {data['distance']}m")
                    if 'angle' in data:
                        details.append(f"Angle: {data['angle']}°")
                    if 'obstacles' in data:
                        details.append(f"Obstacles: {len(data['obstacles'])}")
                    
                    sensor_info += ", ".join(details)
                    context_lines.append(sensor_info)
                else:
                    context_lines.append(f"  {sensor}: {data}")
        
        return "\n".join(context_lines)
    
    def validate_navigation_command(self, nav_command):
        """
        Validate navigation command for safety and feasibility
        """
        warnings = []
        
        # Check speed limits
        if "parameters" in nav_command and "speed" in nav_command["parameters"]:
            speed = float(nav_command["parameters"]["speed"])
            if speed > self.robot_config["max_speed"]:
                nav_command["parameters"]["speed"] = str(self.robot_config["max_speed"])
                warnings.append(f"Speed reduced to maximum safe speed: {self.robot_config['max_speed']} m/s")
        
        # Check for obstacle proximity
        if "obstacles_detected" in nav_command and nav_command["obstacles_detected"]:
            nav_command["safety_status"] = "caution"
            warnings.append("Obstacles detected - proceed with caution")
        
        if warnings:
            nav_command["warnings"] = warnings
        
        return nav_command
    
    def plan_path(self, start_position, target_position, obstacles=None):
        """
        Plan optimal path from start to target position
        """
        context = f"Start: {json.dumps(start_position)}\nTarget: {json.dumps(target_position)}"
        if obstacles:
            context += f"\nObstacles: {json.dumps(obstacles)}"
        
        query = "Plan the optimal path considering robot constraints, obstacles, and safety margins."
        return self.process_query(query, context)
    
    def analyze_sensor_data(self, sensor_readings):
        """
        Analyze sensor data for navigation decisions
        """
        query = "Analyze this sensor data and provide navigation recommendations including obstacle avoidance strategies."
        return self.process_query(query, f"Sensor Readings: {json.dumps(sensor_readings)}")
    
    def update_map(self, new_sensor_data, current_position):
        """
        Update internal map with new sensor data
        """
        context = f"Position: {json.dumps(current_position)}\nNew Sensor Data: {json.dumps(new_sensor_data)}"
        query = "Update the robot's map with this new sensor data and identify any changes in the environment."
        return self.process_query(query, context)
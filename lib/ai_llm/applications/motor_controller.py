from .base_application import BaseAIApplication
import ujson as json

class MotorController(BaseAIApplication):
    """
    AI-powered motor control system with natural language interface
    """
    
    def __init__(self, ai_client, motor_config=None):
        self.motor_config = motor_config or {
            "max_speed": 100,
            "min_speed": 0,
            "max_angle": 180,
            "min_angle": 0,
            "motor_types": ["servo", "stepper", "dc"]
        }
        super().__init__(ai_client, temperature=0.2)  # Low temperature for precise control
    
    def get_default_system_prompt(self):
        return f"""
You are an expert motor control system AI. Your role is to:

1. Interpret natural language commands for motor control
2. Convert user requests into specific motor parameters (speed, direction, angle, duration)
3. Ensure all commands are within safe operating limits
4. Provide clear feedback about motor actions
5. Suggest optimal motor settings for different tasks

Motor Configuration:
- Speed Range: {self.motor_config['min_speed']}-{self.motor_config['max_speed']}%
- Angle Range: {self.motor_config['min_angle']}-{self.motor_config['max_angle']}°
- Supported Types: {', '.join(self.motor_config['motor_types'])}

IMPORTANT RESPONSE FORMAT:
Always respond with a JSON object containing:
{{
    "action": "motor_command",
    "motor_id": "motor_name_or_id",
    "command": "start/stop/set_speed/set_angle/rotate",
    "parameters": {{
        "speed": 0-100,
        "angle": 0-180,
        "direction": "cw/ccw/forward/backward",
        "duration": "seconds or null for continuous"
    }},
    "explanation": "Human-readable explanation of the action",
    "safety_check": "passed/warning/failed",
    "warnings": ["list of any safety warnings"]
}}

If the command is unclear or unsafe, set safety_check to "failed" and explain why.
"""
    
    def process_motor_command(self, user_command, motor_status=None):
        """
        Process natural language motor command
        
        Args:
            user_command: Natural language command (e.g., "turn motor 1 clockwise at 50% speed")
            motor_status: Current motor status dictionary
            
        Returns:
            Parsed motor command dictionary
        """
        context = self.format_motor_context(motor_status)
        response = self.process_query(user_command, context)
        
        if response:
            try:
                # Try to parse JSON response
                import ujson as json
                command_data = json.loads(response)
                return self.validate_motor_command(command_data)
            except:
                # If JSON parsing fails, return error
                return {
                    "action": "error",
                    "explanation": "Failed to parse motor command",
                    "raw_response": response
                }
        
        return None
    
    def format_motor_context(self, motor_status):
        """
        Format current motor status for context
        """
        if not motor_status:
            return "No current motor status available."
        
        context_lines = ["Current Motor Status:"]
        
        for motor_id, status in motor_status.items():
            status_line = f"- {motor_id}: "
            if 'running' in status:
                status_line += f"{'Running' if status['running'] else 'Stopped'}"
            if 'speed' in status:
                status_line += f", Speed: {status['speed']}%"
            if 'angle' in status:
                status_line += f", Angle: {status['angle']}°"
            if 'temperature' in status:
                status_line += f", Temp: {status['temperature']}°C"
            
            context_lines.append(status_line)
        
        return "\n".join(context_lines)
    
    def validate_motor_command(self, command_data):
        """
        Validate motor command parameters
        """
        if not isinstance(command_data, dict):
            return {"action": "error", "explanation": "Invalid command format"}
        
        # Check required fields
        required_fields = ["action", "command", "explanation"]
        for field in required_fields:
            if field not in command_data:
                command_data["safety_check"] = "failed"
                command_data["warnings"] = [f"Missing required field: {field}"]
                return command_data
        
        # Validate parameters if present
        if "parameters" in command_data:
            params = command_data["parameters"]
            warnings = []
            
            # Check speed limits
            if "speed" in params:
                speed = params["speed"]
                if speed < self.motor_config["min_speed"] or speed > self.motor_config["max_speed"]:
                    warnings.append(f"Speed {speed}% is outside safe range {self.motor_config['min_speed']}-{self.motor_config['max_speed']}%")
            
            # Check angle limits
            if "angle" in params:
                angle = params["angle"]
                if angle < self.motor_config["min_angle"] or angle > self.motor_config["max_angle"]:
                    warnings.append(f"Angle {angle}° is outside safe range {self.motor_config['min_angle']}-{self.motor_config['max_angle']}°")
            
            if warnings:
                command_data["safety_check"] = "warning"
                command_data["warnings"] = warnings
        
        return command_data
    
    def get_motor_sequence(self, sequence_description):
        """
        Generate a sequence of motor commands from description
        """
        query = f"Create a sequence of motor commands for: {sequence_description}. Provide each step as a separate JSON command."
        return self.process_query(query)
    
    def optimize_motor_settings(self, task_description, motor_specs=None):
        """
        Get optimized motor settings for a specific task
        """
        context = f"Task: {task_description}"
        if motor_specs:
            context += f"\nMotor Specifications: {motor_specs}"
        
        query = "What are the optimal motor settings (speed, acceleration, etc.) for this task? Consider efficiency and precision."
        return self.process_query(query, context)
from .base_application import BaseAIApplication
import ujson as json

class SmartHomeController(BaseAIApplication):
    """
    AI-powered smart home automation system
    """
    
    def __init__(self, ai_client, home_config=None):
        self.home_config = home_config or {
            "rooms": ["living_room", "bedroom", "kitchen", "bathroom"],
            "devices": {
                "lights": ["main_light", "accent_lights"],
                "climate": ["thermostat", "fan"],
                "appliances": ["tv", "coffee_maker", "washing_machine"],
                "sensors": ["motion", "door", "window", "smoke"]
            },
            "schedules": {},
            "energy_saving": True
        }
        super().__init__(ai_client, temperature=0.3)
    
    def get_default_system_prompt(self):
        return f"""
You are an intelligent smart home automation assistant. Your role is to:

1. Control home devices based on natural language commands
2. Optimize energy usage and comfort
3. Create and manage automation schedules
4. Provide home status reports and recommendations
5. Ensure home security and safety
6. Learn user preferences and adapt accordingly

Home Configuration:
- Rooms: {', '.join(self.home_config['rooms'])}
- Available Devices: {json.dumps(self.home_config['devices'])}
- Energy Saving Mode: {self.home_config['energy_saving']}

RESPONSE FORMAT:
Always respond with a JSON object containing:
{{
    "action": "device_control/schedule/report/recommendation",
    "target": "device_name_or_room",
    "command": "specific_action",
    "parameters": {{
        "value": "setting_value",
        "duration": "time_period",
        "conditions": "trigger_conditions"
    }},
    "explanation": "Human-readable explanation",
    "energy_impact": "low/medium/high",
    "safety_check": "passed/warning/failed",
    "suggestions": ["additional recommendations"]
}}

Prioritize energy efficiency, user comfort, and safety in all recommendations.
"""
    
    def process_home_command(self, user_command, home_status=None):
        """
        Process natural language home automation command
        
        Args:
            user_command: Natural language command
            home_status: Current home device status
            
        Returns:
            Parsed home automation command
        """
        context = self.format_home_context(home_status)
        response = self.process_query(user_command, context)
        
        if response:
            try:
                command_data = json.loads(response)
                return self.validate_home_command(command_data)
            except:
                return {
                    "action": "error",
                    "explanation": "Failed to parse home command",
                    "raw_response": response
                }
        return None
    
    def format_home_context(self, home_status):
        """
        Format current home status for context
        """
        if not home_status:
            return "No current home status available."
        
        context_lines = ["Current Home Status:"]
        
        for room, devices in home_status.items():
            context_lines.append(f"\n{room.title()}:")
            for device, status in devices.items():
                if isinstance(status, dict):
                    status_str = ", ".join([f"{k}: {v}" for k, v in status.items()])
                    context_lines.append(f"  - {device}: {status_str}")
                else:
                    context_lines.append(f"  - {device}: {status}")
        
        return "\n".join(context_lines)
    
    def validate_home_command(self, command_data):
        """
        Validate home automation command
        """
        if not isinstance(command_data, dict):
            return {"action": "error", "explanation": "Invalid command format"}
        
        # Add safety validations
        warnings = []
        
        if command_data.get("action") == "device_control":
            target = command_data.get("target")
            command = command_data.get("command")
            
            # Check for potentially unsafe commands
            if "oven" in target.lower() and "on" in command.lower():
                warnings.append("Oven control requires manual confirmation for safety")
            
            if "door" in target.lower() and "unlock" in command.lower():
                warnings.append("Door unlock command should verify user identity")
        
        if warnings:
            command_data["safety_check"] = "warning"
            command_data["warnings"] = warnings
        
        return command_data
    
    def get_energy_report(self, usage_data):
        """
        Generate energy usage report and recommendations
        """
        query = "Analyze this energy usage data and provide optimization recommendations for reducing consumption while maintaining comfort."
        return self.process_query(query, f"Energy Usage Data: {json.dumps(usage_data)}")
    
    def create_automation_schedule(self, schedule_request):
        """
        Create automation schedules based on user preferences
        """
        query = f"Create a smart home automation schedule for: {schedule_request}. Include optimal timing and energy-efficient settings."
        return self.process_query(query)
    
    def get_comfort_optimization(self, preferences, current_conditions):
        """
        Optimize home settings for comfort
        """
        context = f"User Preferences: {json.dumps(preferences)}\nCurrent Conditions: {json.dumps(current_conditions)}"
        query = "Optimize home settings for maximum comfort while considering energy efficiency."
        return self.process_query(query, context)
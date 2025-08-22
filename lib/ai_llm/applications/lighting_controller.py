from .base_application import BaseAIApplication
import ujson as json

class LightingController(BaseAIApplication):
    """
    AI-powered intelligent lighting system
    """
    
    def __init__(self, ai_client, lighting_config=None):
        self.lighting_config = lighting_config or {
            "zones": ["living_room", "bedroom", "kitchen", "outdoor"],
            "light_types": ["main", "accent", "task", "ambient"],
            "features": ["dimming", "color_change", "scheduling", "motion_detection"],
            "energy_efficiency": True,
            "circadian_rhythm": True
        }
        super().__init__(ai_client, temperature=0.4)
    
    def get_default_system_prompt(self):
        return f"""
You are an intelligent lighting control system AI. Your responsibilities include:

1. Optimizing lighting for comfort, productivity, and energy efficiency
2. Adjusting lighting based on time of day, activity, and user preferences
3. Supporting circadian rhythm with appropriate color temperatures
4. Creating dynamic lighting scenes and schedules
5. Responding to natural language lighting commands
6. Providing energy usage insights and recommendations

Lighting Configuration:
- Zones: {', '.join(self.lighting_config['zones'])}
- Light Types: {', '.join(self.lighting_config['light_types'])}
- Features: {', '.join(self.lighting_config['features'])}
- Circadian Support: {self.lighting_config['circadian_rhythm']}

RESPONSE FORMAT:
Always respond with a JSON object containing:
{{
    "action": "set_brightness/set_color/create_scene/schedule",
    "zone": "target_zone_or_all",
    "lights": ["specific_light_ids"],
    "parameters": {{
        "brightness": "0-100_percent",
        "color_temp": "2700-6500_kelvin",
        "rgb_color": "[r,g,b]_values",
        "transition_time": "seconds",
        "schedule": "time_based_rules"
    }},
    "explanation": "reason_for_lighting_choice",
    "energy_impact": "estimated_power_usage",
    "circadian_benefit": "health_and_wellness_impact",
    "scene_name": "descriptive_scene_name"
}}

Optimize for user comfort, energy efficiency, and health benefits.
"""
    
    def process_lighting_command(self, user_command, current_status=None, time_context=None):
        """
        Process natural language lighting commands
        
        Args:
            user_command: Natural language lighting request
            current_status: Current lighting status
            time_context: Time of day and activity context
            
        Returns:
            Lighting control commands
        """
        context = self.format_lighting_context(current_status, time_context)
        response = self.process_query(user_command, context)
        
        if response:
            try:
                lighting_command = json.loads(response)
                return self.optimize_lighting_command(lighting_command)
            except:
                return {
                    "action": "error",
                    "explanation": "Failed to parse lighting command",
                    "raw_response": response
                }
        return None
    
    def format_lighting_context(self, current_status, time_context):
        """
        Format current lighting and time context
        """
        context_lines = []
        
        if time_context:
            context_lines.append(f"Time Context: {json.dumps(time_context)}")
        
        if current_status:
            context_lines.append("Current Lighting Status:")
            for zone, lights in current_status.items():
                context_lines.append(f"  {zone}:")
                for light_id, status in lights.items():
                    if isinstance(status, dict):
                        status_str = ", ".join([f"{k}: {v}" for k, v in status.items()])
                        context_lines.append(f"    - {light_id}: {status_str}")
                    else:
                        context_lines.append(f"    - {light_id}: {status}")
        
        return "\n".join(context_lines)
    
    def optimize_lighting_command(self, lighting_command):
        """
        Optimize lighting command for energy efficiency and comfort
        """
        # Add energy optimization suggestions
        if "parameters" in lighting_command:
            params = lighting_command["parameters"]
            
            # Suggest energy-efficient brightness levels
            if "brightness" in params:
                brightness = int(params["brightness"])
                if brightness > 80:
                    lighting_command["energy_suggestion"] = "Consider 70-80% brightness for energy savings"
        
        return lighting_command
    
    def create_circadian_schedule(self, user_schedule, preferences=None):
        """
        Create circadian rhythm-supporting lighting schedule
        """
        context = f"User Schedule: {json.dumps(user_schedule)}"
        if preferences:
            context += f"\nUser Preferences: {json.dumps(preferences)}"
        
        query = "Create a circadian rhythm lighting schedule that supports natural sleep-wake cycles and productivity."
        return self.process_query(query, context)
    
    def analyze_lighting_usage(self, usage_data, time_period):
        """
        Analyze lighting usage patterns and provide optimization recommendations
        """
        context = f"Usage Data: {json.dumps(usage_data)}\nTime Period: {time_period}"
        query = "Analyze lighting usage patterns and recommend optimizations for energy savings and improved comfort."
        return self.process_query(query, context)
    
    def suggest_lighting_scene(self, activity, mood=None, occupancy=None):
        """
        Suggest optimal lighting scene for specific activities
        """
        context = f"Activity: {activity}"
        if mood:
            context += f"\nDesired Mood: {mood}"
        if occupancy:
            context += f"\nRoom Occupancy: {occupancy}"
        
        query = "Suggest the optimal lighting scene (brightness, color temperature, zones) for this activity and mood."
        return self.process_query(query, context)
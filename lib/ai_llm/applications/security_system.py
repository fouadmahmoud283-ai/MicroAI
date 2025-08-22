from .base_application import BaseAIApplication
import ujson as json

class SecuritySystem(BaseAIApplication):
    """
    AI-powered home security and monitoring system
    """
    
    def __init__(self, ai_client, security_config=None):
        self.security_config = security_config or {
            "zones": ["entry", "perimeter", "interior", "garage"],
            "sensors": ["motion", "door", "window", "camera", "smoke", "glass_break"],
            "alert_levels": ["info", "warning", "critical", "emergency"],
            "response_protocols": ["notify", "alarm", "call_authorities"],
            "authorized_users": []
        }
        super().__init__(ai_client, temperature=0.1)  # Very low temperature for security
    
    def get_default_system_prompt(self):
        return f"""
You are an expert security system AI responsible for:

1. Analyzing security sensor data and events
2. Detecting potential threats and anomalies
3. Determining appropriate response levels
4. Providing security recommendations
5. Managing access control and user authentication
6. Generating security reports and alerts

Security Configuration:
- Monitored Zones: {', '.join(self.security_config['zones'])}
- Sensor Types: {', '.join(self.security_config['sensors'])}
- Alert Levels: {', '.join(self.security_config['alert_levels'])}

RESPONSE FORMAT:
Always respond with a JSON object containing:
{{
    "threat_level": "none/low/medium/high/critical",
    "alert_type": "info/warning/critical/emergency",
    "zone": "affected_security_zone",
    "description": "detailed_threat_description",
    "recommended_actions": ["list_of_actions"],
    "confidence": "0-100_percent",
    "requires_human_verification": true/false,
    "emergency_response": "none/notify/alarm/authorities",
    "additional_monitoring": ["sensors_to_activate"]
}}

Prioritize safety and security. When in doubt, escalate to higher alert levels.
"""
    
    def analyze_security_event(self, sensor_data, event_type="unknown"):
        """
        Analyze security sensor data and events
        
        Args:
            sensor_data: Dictionary with sensor readings and events
            event_type: Type of security event
            
        Returns:
            Security analysis and response recommendations
        """
        formatted_data = self.format_security_data(sensor_data, event_type)
        query = "Analyze this security event data and determine the threat level and appropriate response."
        
        response = self.process_query(query, formatted_data)
        
        if response:
            try:
                security_analysis = json.loads(response)
                return self.validate_security_response(security_analysis)
            except:
                # Fallback for critical security situations
                return {
                    "threat_level": "medium",
                    "alert_type": "warning",
                    "description": "Security analysis failed - manual review required",
                    "recommended_actions": ["Manual security check", "Review sensor data"],
                    "requires_human_verification": True
                }
        
        return None
    
    def format_security_data(self, sensor_data, event_type):
        """
        Format security sensor data for analysis
        """
        formatted = [f"Event Type: {event_type}"]
        
        for sensor, data in sensor_data.items():
            if isinstance(data, dict):
                sensor_info = f"{sensor}: "
                details = []
                
                if 'status' in data:
                    details.append(f"Status: {data['status']}")
                if 'value' in data:
                    details.append(f"Value: {data['value']}")
                if 'timestamp' in data:
                    details.append(f"Time: {data['timestamp']}")
                if 'zone' in data:
                    details.append(f"Zone: {data['zone']}")
                
                sensor_info += ", ".join(details)
                formatted.append(sensor_info)
            else:
                formatted.append(f"{sensor}: {data}")
        
        return "\n".join(formatted)
    
    def validate_security_response(self, security_analysis):
        """
        Validate and enhance security response
        """
        # Ensure critical fields are present
        required_fields = ["threat_level", "alert_type", "description"]
        for field in required_fields:
            if field not in security_analysis:
                security_analysis[field] = "unknown"
        
        # Auto-escalate if confidence is low on high-threat events
        if (security_analysis.get("threat_level") in ["high", "critical"] and 
            int(security_analysis.get("confidence", 0)) < 70):
            security_analysis["requires_human_verification"] = True
        
        return security_analysis
    
    def check_access_control(self, user_id, access_request, biometric_data=None):
        """
        Verify user access permissions
        """
        context = f"User ID: {user_id}\nAccess Request: {access_request}"
        if biometric_data:
            context += f"\nBiometric Data: {json.dumps(biometric_data)}"
        
        query = "Verify if this user should be granted access based on their credentials and the security context."
        return self.process_query(query, context)
    
    def generate_security_report(self, time_period, incident_data):
        """
        Generate comprehensive security report
        """
        context = f"Time Period: {time_period}\nIncident Data: {json.dumps(incident_data)}"
        query = "Generate a comprehensive security report including threat analysis, patterns, and recommendations for improvement."
        return self.process_query(query, context)
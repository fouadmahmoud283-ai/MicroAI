from .base_application import BaseAIApplication
import ujson as json

class WeatherAnalyzer(BaseAIApplication):
    """
    AI-powered weather sensor data analyzer
    """
    
    def __init__(self, ai_client, location="Unknown", units="metric"):
        self.location = location
        self.units = units
        super().__init__(ai_client, temperature=0.3)  # Lower temperature for more consistent analysis
    
    def get_default_system_prompt(self):
        return f"""
You are an expert weather data analyst and meteorologist. Your role is to:

1. Analyze weather sensor data (temperature, humidity, pressure, wind, etc.)
2. Provide insights about current weather conditions
3. Suggest actions based on weather data (irrigation, heating/cooling, etc.)
4. Detect anomalies or concerning patterns in sensor readings
5. Give weather-related recommendations for outdoor activities or equipment operation

Location: {self.location}
Units: {self.units}

Always provide:
- Clear analysis of the data
- Practical recommendations
- Any warnings about extreme conditions
- Confidence level in your analysis

Respond in a concise, actionable format suitable for IoT device displays.
"""
    
    def analyze_sensor_data(self, sensor_data, query=None):
        """
        Analyze weather sensor data
        
        Args:
            sensor_data: Dictionary with sensor readings
            query: Optional specific question about the data
            
        Returns:
            Analysis and recommendations
        """
        if not query:
            query = "Analyze this weather data and provide insights and recommendations."
        
        formatted_data = self.format_sensor_data(sensor_data)
        return self.process_query(query, formatted_data)
    
    def format_sensor_data(self, sensor_data):
        """
        Format sensor data for AI analysis
        """
        formatted = []
        
        # Temperature data
        if 'temperature' in sensor_data:
            temp = sensor_data['temperature']
            unit = "°C" if self.units == "metric" else "°F"
            formatted.append(f"Temperature: {temp}{unit}")
        
        # Humidity data
        if 'humidity' in sensor_data:
            formatted.append(f"Humidity: {sensor_data['humidity']}%")
        
        # Pressure data
        if 'pressure' in sensor_data:
            pressure_unit = "hPa" if self.units == "metric" else "inHg"
            formatted.append(f"Pressure: {sensor_data['pressure']} {pressure_unit}")
        
        # Wind data
        if 'wind_speed' in sensor_data:
            wind_unit = "m/s" if self.units == "metric" else "mph"
            formatted.append(f"Wind Speed: {sensor_data['wind_speed']} {wind_unit}")
        
        if 'wind_direction' in sensor_data:
            formatted.append(f"Wind Direction: {sensor_data['wind_direction']}°")
        
        # Additional sensors
        for key, value in sensor_data.items():
            if key not in ['temperature', 'humidity', 'pressure', 'wind_speed', 'wind_direction']:
                formatted.append(f"{key.replace('_', ' ').title()}: {value}")
        
        # Add timestamp if available
        if 'timestamp' in sensor_data:
            formatted.append(f"Reading Time: {sensor_data['timestamp']}")
        
        return "\n".join(formatted)
    
    def get_irrigation_recommendation(self, sensor_data, crop_type="general"):
        """
        Get irrigation recommendations based on weather data
        """
        query = f"Based on this weather data, should I irrigate my {crop_type} crops? Consider soil moisture needs and weather conditions."
        return self.analyze_sensor_data(sensor_data, query)
    
    def get_hvac_recommendation(self, sensor_data, target_temp=22):
        """
        Get HVAC system recommendations
        """
        query = f"Based on this weather data, what HVAC adjustments should I make to maintain {target_temp}°C indoor temperature efficiently?"
        return self.analyze_sensor_data(sensor_data, query)
    
    def detect_weather_alerts(self, sensor_data):
        """
        Detect potential weather alerts or warnings
        """
        query = "Analyze this weather data for any extreme conditions, alerts, or warnings I should be aware of. Focus on safety and equipment protection."
        return self.analyze_sensor_data(sensor_data, query)
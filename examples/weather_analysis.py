import sys
sys.path.append('/lib')

from ai_llm import AIClient, ModelConfig, WeatherAnalyzer

def main():
    # Setup AI client
    client = AIClient(
        api_key="your-api-key-here",
        model_config=ModelConfig(model_name="gpt-3.5-turbo")
    )
    
    # Create weather analyzer
    weather_ai = WeatherAnalyzer(
        ai_client=client,
        location="Garden Greenhouse",
        units="metric"
    )
    
    # Sample sensor data
    sensor_data = {
        "temperature": 28.5,
        "humidity": 65,
        "pressure": 1013.2,
        "soil_moisture": 45,
        "light_level": 850,
        "timestamp": "2024-01-15 14:30:00"
    }
    
    # General analysis
    print("=== Weather Analysis ===")
    analysis = weather_ai.analyze_sensor_data(sensor_data)
    print(analysis)
    
    # Irrigation recommendation
    print("\n=== Irrigation Recommendation ===")
    irrigation = weather_ai.get_irrigation_recommendation(sensor_data, "tomatoes")
    print(irrigation)
    
    # Weather alerts
    print("\n=== Weather Alerts ===")
    alerts = weather_ai.detect_weather_alerts(sensor_data)
    print(alerts)

if __name__ == "__main__":
    main()
"""
Example usage of EnergyMonitorApp for utility monitoring and cost analysis
"""

from lib.ai_llm.client import AIClient
from lib.ai_llm.applications.energy_monitor import EnergyMonitorApp


def main():
    # Initialize AI client
    ai_client = AIClient(api_key="your-api-key")
    
    # Configure energy monitor
    config = {
        "utility_types": ["electricity", "water", "gas"],
        "rate_costs": {
            "electricity": {"per_unit": 0.12, "currency": "USD", "unit": "kWh"},
            "water": {"per_unit": 0.005, "currency": "USD", "unit": "gallon"},
            "gas": {"per_unit": 1.50, "currency": "USD", "unit": "therm"}
        },
        "monitoring_preferences": {
            "detect_anomalies": True,
            "compare_periods": True,
            "alert_thresholds": {
                "electricity": {"high_usage_percent": 20, "high_cost_percent": 25},
                "water": {"high_usage_percent": 15, "high_cost_percent": 20},
                "gas": {"high_usage_percent": 25, "high_cost_percent": 30}
            }
        }
    }
    
    # Create energy monitor app
    energy_monitor = EnergyMonitorApp(ai_client, config)
    
    # Example consumption data
    consumption_data = {
        "electricity": {
            "usage": 450,
            "peak_usage": 280,
            "off_peak_usage": 170
        },
        "water": {
            "usage": 2500,
            "peak_usage": 1500
        },
        "gas": {
            "usage": 45,
            "heating_degree_days": 1200
        },
        "timestamp": "2024-01-15T10:30:00Z",
        "period": "January 2024"
    }
    
    print("=" * 60)
    print("ENERGY MONITOR APP - UTILITY MONITORING EXAMPLE")
    print("=" * 60)
    
    # Analyze consumption
    print("\n1. ANALYZING CONSUMPTION DATA...")
    analysis = energy_monitor.analyze_consumption(consumption_data)
    if analysis:
        print(f"   Analysis: {analysis.get('summary', 'N/A')}")
        print(f"   Confidence: {analysis.get('confidence_level', 'N/A')}")
    
    # Get cost estimate
    print("\n2. CALCULATING COST ESTIMATE...")
    cost_estimate = energy_monitor.get_cost_estimate(consumption_data)
    if cost_estimate and "cost_breakdown" in cost_estimate:
        breakdown = cost_estimate["cost_breakdown"]
        print(f"   Total Cost: {breakdown.get('currency', 'USD')} {breakdown.get('total_cost', 0)}")
        print("   By Utility:")
        for utility, data in breakdown.get("by_utility", {}).items():
            print(f"     - {utility}: {data.get('usage', 0)} {data.get('unit', 'units')} = {data.get('cost', 0)}")
    
    # Get optimization recommendations
    print("\n3. GETTING OPTIMIZATION RECOMMENDATIONS...")
    recommendations = energy_monitor.get_optimization_recommendations(consumption_data)
    if recommendations and "recommendations" in recommendations:
        print("   Top Recommendations:")
        for i, rec in enumerate(recommendations["recommendations"][:3], 1):
            print(f"     {i}. {rec}")
    
    # Detect anomalies
    print("\n4. DETECTING ANOMALIES...")
    anomalies = energy_monitor.detect_anomalies(consumption_data)
    if anomalies and "anomalies" in anomalies:
        if anomalies["anomalies"]:
            print("   Detected Anomalies:")
            for anomaly in anomalies["anomalies"]:
                print(f"     - [{anomaly.get('severity', 'unknown').upper()}] {anomaly.get('description', 'N/A')}")
        else:
            print("   No anomalies detected")
    
    # Compare periods
    print("\n5. COMPARING PERIODS...")
    previous_data = {
        "electricity": {"usage": 400},
        "water": {"usage": 2200},
        "gas": {"usage": 50}
    }
    comparison = energy_monitor.compare_periods(consumption_data, previous_data)
    if comparison and "comparison" in comparison:
        comp = comparison["comparison"]
        print(f"   Usage Change: {comp.get('period_change_percent', 0):+.1f}%")
        print(f"   Cost Change: {comp.get('cost_change_percent', 0):+.1f}%")
        if comp.get("significant_differences"):
            print("   Significant Differences:")
            for diff in comp["significant_differences"]:
                print(f"     - {diff}")
    
    print("\n" + "=" * 60)
    print("EXAMPLE COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()

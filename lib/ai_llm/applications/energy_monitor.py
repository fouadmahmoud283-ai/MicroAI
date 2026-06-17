from .base_application import BaseAIApplication
import ujson as json


class EnergyMonitorApp(BaseAIApplication):
    """
    AI-powered utility monitoring system for electricity, water, and gas
    """
    
    def __init__(self, ai_client, config=None):
        self.config = config or {}
        self.utility_types = self.config.get("utility_types", ["electricity", "water", "gas"])
        self.rate_costs = self.config.get("rate_costs", {
            "electricity": {"per_unit": 0.12, "currency": "USD", "unit": "kWh"},
            "water": {"per_unit": 0.005, "currency": "USD", "unit": "gallon"},
            "gas": {"per_unit": 1.50, "currency": "USD", "unit": "therm"}
        })
        self.monitoring_preferences = self.config.get("monitoring_preferences", {
            "detect_anomalies": True,
            "compare_periods": True,
            "include_forecasts": False,
            "alert_thresholds": {
                "electricity": {"high_usage_percent": 20, "high_cost_percent": 25},
                "water": {"high_usage_percent": 15, "high_cost_percent": 20},
                "gas": {"high_usage_percent": 25, "high_cost_percent": 30}
            }
        })
        super().__init__(ai_client, temperature=0.3)
    
    def get_default_system_prompt(self):
        return f"""
You are an expert utility monitoring and cost optimization specialist. Your role is to:

1. Analyze consumption data for electricity, water, and gas utilities
2. Calculate costs with rate tier considerations
3. Detect anomalies and unusual usage patterns
4. Provide optimization recommendations for reducing costs
5. Compare usage between different time periods
6. Identify opportunities for efficiency improvements

Monitored Utilities: {', '.join(self.utility_types)}

Rate Configuration:
{json.dumps(self.rate_costs, indent=2)}

Monitoring Preferences:
{json.dumps(self.monitoring_preferences, indent=2)}

RESPONSE FORMAT:
Always respond with a valid JSON object containing:
{{
    "analysis": "Detailed analysis of consumption patterns",
    "cost_breakdown": {{
        "total_cost": number,
        "by_utility": {{
            "electricity": {{"usage": number, "cost": number}},
            "water": {{"usage": number, "cost": number}},
            "gas": {{"usage": number, "cost": number}}
        }},
        "rate_tiers_applied": ["list of applicable rate tiers"],
        "currency": "USD"
    }},
    "recommendations": ["list of specific cost-saving recommendations"],
    "anomalies": [
        {{
            "utility": "utility_type",
            "description": "description of anomaly",
            "severity": "low/medium/high",
            "potential_cause": "possible explanation"
        }}
    ],
    "comparison": {{
        "period_change_percent": number,
        "cost_change_percent": number,
        "significant_differences": ["list of notable changes"]
    }},
    "confidence_level": "high/medium/low",
    "summary": "Brief executive summary"
}}

Prioritize actionable insights, cost savings, and anomaly detection in all responses.
"""
    
    def analyze_consumption(self, consumption_data):
        """
        Analyze utility consumption data
        
        Args:
            consumption_data: Dictionary containing utility consumption readings
            
        Returns:
            JSON response with analysis and recommendations
        """
        formatted_data = self.format_consumption_data(consumption_data)
        query = "Analyze this utility consumption data. Provide insights on usage patterns, cost implications, and recommendations for optimization."
        response = self.process_query(query, formatted_data)
        
        if response:
            try:
                return json.loads(response)
            except (json.JSONDecodeError, TypeError):
                return {
                    "analysis": response,
                    "cost_breakdown": {},
                    "recommendations": [],
                    "anomalies": [],
                    "confidence_level": "medium",
                    "summary": "Analysis completed with parsing limitations"
                }
        return None
    
    def get_cost_estimate(self, consumption_data):
        """
        Calculate cost estimates for utility consumption
        
        Args:
            consumption_data: Dictionary with usage values for each utility
            
        Returns:
            JSON response with detailed cost breakdown
        """
        formatted_data = self.format_consumption_data(consumption_data)
        query = "Calculate the cost estimates for this utility consumption. Include rate tier calculations, total costs, and per-utility breakdowns."
        response = self.process_query(query, formatted_data)
        
        if response:
            try:
                return json.loads(response)
            except (json.JSONDecodeError, TypeError):
                return self._calculate_cost_estimate_direct(consumption_data)
        return None
    
    def _calculate_cost_estimate_direct(self, consumption_data):
        """
        Direct cost calculation without AI (fallback)
        """
        cost_breakdown = {
            "total_cost": 0,
            "by_utility": {},
            "rate_tiers_applied": ["standard"],
            "currency": self.rate_costs.get("electricity", {}).get("currency", "USD")
        }
        
        for utility in self.utility_types:
            if utility in consumption_data:
                usage = consumption_data[utility]
                rate_info = self.rate_costs.get(utility, {})
                per_unit = rate_info.get("per_unit", 0)
                cost = usage * per_unit
                
                cost_breakdown["by_utility"][utility] = {
                    "usage": usage,
                    "cost": round(cost, 2),
                    "unit": rate_info.get("unit", "units")
                }
                cost_breakdown["total_cost"] += cost
        
        cost_breakdown["total_cost"] = round(cost_breakdown["total_cost"], 2)
        
        return {
            "analysis": "Cost estimate calculated using standard rates",
            "cost_breakdown": cost_breakdown,
            "recommendations": self._get_basic_recommendations(consumption_data),
            "anomalies": [],
            "confidence_level": "high",
            "summary": f"Total estimated cost: {cost_breakdown['currency']} {cost_breakdown['total_cost']}"
        }
    
    def get_optimization_recommendations(self, consumption_data):
        """
        Get cost-saving optimization recommendations
        
        Args:
            consumption_data: Dictionary with utility consumption data
            
        Returns:
            JSON response with actionable recommendations
        """
        formatted_data = self.format_consumption_data(consumption_data)
        query = "Provide specific, actionable recommendations for reducing utility costs. Focus on behavioral changes, efficiency upgrades, and usage optimization."
        response = self.process_query(query, formatted_data)
        
        if response:
            try:
                return json.loads(response)
            except (json.JSONDecodeError, TypeError):
                return {
                    "analysis": response,
                    "cost_breakdown": {},
                    "recommendations": self._get_basic_recommendations(consumption_data),
                    "anomalies": [],
                    "confidence_level": "medium",
                    "summary": "Recommendations provided with formatting limitations"
                }
        return None
    
    def detect_anomalies(self, consumption_data):
        """
        Detect unusual usage patterns or anomalies
        
        Args:
            consumption_data: Dictionary with utility consumption data
            
        Returns:
            JSON response with detected anomalies
        """
        formatted_data = self.format_consumption_data(consumption_data)
        query = "Analyze this consumption data for anomalies, unusual spikes, or concerning patterns. Identify potential causes and severity levels."
        response = self.process_query(query, formatted_data)
        
        if response:
            try:
                return json.loads(response)
            except (json.JSONDecodeError, TypeError):
                return {
                    "analysis": "Anomaly detection completed",
                    "cost_breakdown": {},
                    "recommendations": [],
                    "anomalies": self._detect_basic_anomalies(consumption_data),
                    "confidence_level": "medium",
                    "summary": "Basic anomaly detection performed"
                }
        return None
    
    def compare_periods(self, current_data, previous_data):
        """
        Compare usage between two time periods
        
        Args:
            current_data: Current period consumption data
            previous_data: Previous period consumption data
            
        Returns:
            JSON response with comparison analysis
        """
        formatted_current = self.format_consumption_data(current_data)
        formatted_previous = self.format_consumption_data(previous_data)
        
        context = f"Current Period Data:\n{formatted_current}\n\nPrevious Period Data:\n{formatted_previous}"
        query = "Compare these two periods of utility consumption. Calculate percentage changes, identify significant differences, and explain what might have caused any variations."
        response = self.process_query(query, context)
        
        if response:
            try:
                return json.loads(response)
            except (json.JSONDecodeError, TypeError):
                return self._compare_periods_direct(current_data, previous_data)
        return None
    
    def format_consumption_data(self, consumption_data):
        """
        Format consumption data for AI analysis
        
        Args:
            consumption_data: Dictionary with utility readings
            
        Returns:
            Formatted string for AI context
        """
        formatted = []
        
        # Electricity data
        if "electricity" in consumption_data:
            elec = consumption_data["electricity"]
            rate_info = self.rate_costs.get("electricity", {})
            unit = rate_info.get("unit", "kWh")
            if isinstance(elec, dict):
                formatted.append(f"Electricity: {elec.get('usage', elec.get('value', 0))} {unit}")
                if "peak_usage" in elec:
                    formatted.append(f"  Peak Usage: {elec['peak_usage']} {unit}")
                if "off_peak_usage" in elec:
                    formatted.append(f"  Off-Peak Usage: {elec['off_peak_usage']} {unit}")
            else:
                formatted.append(f"Electricity: {elec} {unit}")
        
        # Water data
        if "water" in consumption_data:
            water = consumption_data["water"]
            rate_info = self.rate_costs.get("water", {})
            unit = rate_info.get("unit", "gallons")
            if isinstance(water, dict):
                formatted.append(f"Water: {water.get('usage', water.get('value', 0))} {unit}")
                if "peak_usage" in water:
                    formatted.append(f"  Peak Usage: {water['peak_usage']} {unit}")
            else:
                formatted.append(f"Water: {water} {unit}")
        
        # Gas data
        if "gas" in consumption_data:
            gas = consumption_data["gas"]
            rate_info = self.rate_costs.get("gas", {})
            unit = rate_info.get("unit", "therms")
            if isinstance(gas, dict):
                formatted.append(f"Gas: {gas.get('usage', gas.get('value', 0))} {unit}")
                if "heating_degree_days" in gas:
                    formatted.append(f"  Heating Degree Days: {gas['heating_degree_days']}")
            else:
                formatted.append(f"Gas: {gas} {unit}")
        
        # Additional consumption data
        for key, value in consumption_data.items():
            if key not in ["electricity", "water", "gas"]:
                if isinstance(value, dict):
                    formatted.append(f"{key.replace('_', ' ').title()}: {json.dumps(value)}")
                else:
                    formatted.append(f"{key.replace('_', ' ').title()}: {value}")
        
        # Add timestamp if available
        if "timestamp" in consumption_data:
            formatted.append(f"Reading Time: {consumption_data['timestamp']}")
        
        if "period" in consumption_data:
            formatted.append(f"Period: {consumption_data['period']}")
        
        return "\n".join(formatted)
    
    def _detect_basic_anomalies(self, consumption_data):
        """
        Basic anomaly detection without AI (fallback)
        """
        anomalies = []
        thresholds = self.monitoring_preferences.get("alert_thresholds", {})
        
        for utility in self.utility_types:
            if utility in consumption_data:
                data = consumption_data[utility]
                usage = data.get("usage", data.get("value", 0)) if isinstance(data, dict) else data
                threshold = thresholds.get(utility, {}).get("high_usage_percent", 20)
                
                # Simple heuristic: flag if usage seems unusually high
                if usage > 1000 and utility == "electricity":
                    anomalies.append({
                        "utility": utility,
                        "description": f"High electricity usage detected: {usage} kWh",
                        "severity": "medium",
                        "potential_cause": "Possible appliance malfunction or extended usage"
                    })
                elif usage > 5000 and utility == "water":
                    anomalies.append({
                        "utility": utility,
                        "description": f"High water usage detected: {usage} gallons",
                        "severity": "medium",
                        "potential_cause": "Possible leak or irrigation system running"
                    })
                elif usage > 100 and utility == "gas":
                    anomalies.append({
                        "utility": utility,
                        "description": f"High gas usage detected: {usage} therms",
                        "severity": "medium",
                        "potential_cause": "Possible heating system inefficiency"
                    })
        
        return anomalies
    
    def _compare_periods_direct(self, current_data, previous_data):
        """
        Direct period comparison without AI (fallback)
        """
        comparison = {
            "period_change_percent": 0,
            "cost_change_percent": 0,
            "significant_differences": []
        }
        
        current_cost = 0
        previous_cost = 0
        total_usage_change = 0
        total_previous_usage = 0
        
        for utility in self.utility_types:
            current = current_data.get(utility, {})
            previous = previous_data.get(utility, {})
            
            current_usage = current.get("usage", current.get("value", 0)) if isinstance(current, dict) else current
            previous_usage = previous.get("usage", previous.get("value", 0)) if isinstance(previous, dict) else previous
            
            if previous_usage > 0:
                change_percent = ((current_usage - previous_usage) / previous_usage) * 100
                if abs(change_percent) > 10:
                    comparison["significant_differences"].append(
                        f"{utility}: {change_percent:+.1f}% change ({previous_usage} -> {current_usage})"
                    )
                
                total_usage_change += current_usage - previous_usage
                total_previous_usage += previous_usage
                
                rate = self.rate_costs.get(utility, {}).get("per_unit", 0)
                current_cost += current_usage * rate
                previous_cost += previous_usage * rate
        
        if total_previous_usage > 0:
            comparison["period_change_percent"] = round((total_usage_change / total_previous_usage) * 100, 2)
        
        if previous_cost > 0:
            comparison["cost_change_percent"] = round(((current_cost - previous_cost) / previous_cost) * 100, 2)
        
        return {
            "analysis": "Period comparison completed using direct calculation",
            "cost_breakdown": {
                "current_cost": round(current_cost, 2),
                "previous_cost": round(previous_cost, 2),
                "currency": self.rate_costs.get("electricity", {}).get("currency", "USD")
            },
            "recommendations": [],
            "anomalies": [],
            "comparison": comparison,
            "confidence_level": "high",
            "summary": f"Usage changed by {comparison['period_change_percent']:+.1f}%, cost changed by {comparison['cost_change_percent']:+.1f}%"
        }
    
    def _get_basic_recommendations(self, consumption_data):
        """
        Basic recommendations without AI (fallback)
        """
        recommendations = []
        
        for utility in consumption_data:
            if utility == "electricity":
                recommendations.append("Consider upgrading to energy-efficient LED bulbs")
                recommendations.append("Use smart power strips to reduce phantom load")
            elif utility == "water":
                recommendations.append("Install low-flow fixtures to reduce water usage")
                recommendations.append("Check for leaks in plumbing fixtures")
            elif utility == "gas":
                recommendations.append("Consider upgrading to a high-efficiency furnace")
                recommendations.append("Add weatherstripping to reduce heating costs")
        
        return recommendations

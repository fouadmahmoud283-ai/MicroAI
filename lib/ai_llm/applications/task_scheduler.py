from .base_application import BaseAIApplication
import ujson as json

class TaskScheduler(BaseAIApplication):
    """
    AI-powered task scheduling and automation system
    """
    
    def __init__(self, ai_client, scheduler_config=None):
        self.scheduler_config = scheduler_config or {
            "task_types": ["cleaning", "maintenance", "monitoring", "data_collection"],
            "priority_levels": ["low", "medium", "high", "critical"],
            "scheduling_modes": ["time_based", "event_based", "condition_based"],
            "max_concurrent_tasks": 5,
            "energy_optimization": True
        }
        super().__init__(ai_client, temperature=0.3)
    
    def get_default_system_prompt(self):
        return f"""
You are an intelligent task scheduling and automation AI. Your responsibilities include:

1. Creating optimal task schedules based on priorities and constraints
2. Managing task dependencies and resource allocation
3. Adapting schedules based on real-time conditions
4. Optimizing for energy efficiency and system performance
5. Handling task conflicts and rescheduling
6. Providing task status reports and recommendations

Scheduler Configuration:
- Task Types: {', '.join(self.scheduler_config['task_types'])}
- Priority Levels: {', '.join(self.scheduler_config['priority_levels'])}
- Max Concurrent Tasks: {self.scheduler_config['max_concurrent_tasks']}
- Energy Optimization: {self.scheduler_config['energy_optimization']}

RESPONSE FORMAT:
Always respond with a JSON object containing:
{{
    "schedule_action": "create/modify/cancel/execute",
    "task_id": "unique_task_identifier",
    "task_details": {{
        "name": "task_name",
        "type": "task_category",
        "priority": "low/medium/high/critical",
        "estimated_duration": "minutes",
        "resource_requirements": ["required_resources"],
        "dependencies": ["prerequisite_tasks"]
    }},
    "scheduling": {{
        "start_time": "scheduled_start_time",
        "frequency": "once/daily/weekly/custom",
        "conditions": ["trigger_conditions"]
    }},
    "optimization": {{
        "energy_impact": "low/medium/high",
        "performance_impact": "minimal/moderate/significant",
        "alternative_times": ["backup_scheduling_options"]
    }},
    "explanation": "reasoning_for_scheduling_decision"
}}

Optimize for efficiency, resource utilization, and system performance.
"""
    
    def create_task_schedule(self, task_request, system_status=None, constraints=None):
        """
        Create optimized task schedule
        
        Args:
            task_request: Natural language task scheduling request
            system_status: Current system status and resource availability
            constraints: Scheduling constraints and preferences
            
        Returns:
            Optimized task schedule
        """
        context = self.format_scheduling_context(system_status, constraints)
        response = self.process_query(task_request, context)
        
        if response:
            try:
                schedule_data = json.loads(response)
                return self.optimize_schedule(schedule_data)
            except:
                return {
                    "schedule_action": "error",
                    "explanation": "Failed to create task schedule",
                    "raw_response": response
                }
        return None
    
    def format_scheduling_context(self, system_status, constraints):
        """
        Format system status and constraints for scheduling context
        """
        context_lines = []
        
        if system_status:
            context_lines.append("System Status:")
            for component, status in system_status.items():
                if isinstance(status, dict):
                    status_str = ", ".join([f"{k}: {v}" for k, v in status.items()])
                    context_lines.append(f"  {component}: {status_str}")
                else:
                    context_lines.append(f"  {component}: {status}")
        
        if constraints:
            context_lines.append(f"\nScheduling Constraints: {json.dumps(constraints)}")
        
        return "\n".join(context_lines)
    
    def optimize_schedule(self, schedule_data):
        """
        Optimize schedule for efficiency and resource utilization
        """
        # Add optimization suggestions
        if "task_details" in schedule_data:
            task = schedule_data["task_details"]
            
            # Suggest energy-efficient scheduling
            if self.scheduler_config["energy_optimization"]:
                if "optimization" not in schedule_data:
                    schedule_data["optimization"] = {}
                
                schedule_data["optimization"]["energy_suggestion"] = "Consider scheduling during off-peak hours for energy savings"
        
        return schedule_data
    
    def handle_task_conflict(self, conflicting_tasks, available_resources):
        """
        Resolve task scheduling conflicts
        """
        context = f"Conflicting Tasks: {json.dumps(conflicting_tasks)}\nAvailable Resources: {json.dumps(available_resources)}"
        query = "Resolve these task scheduling conflicts by prioritizing, rescheduling, or resource reallocation."
        return self.process_query(query, context)
    
    def adapt_schedule(self, current_schedule, new_conditions):
        """
        Adapt existing schedule to new conditions
        """
        context = f"Current Schedule: {json.dumps(current_schedule)}\nNew Conditions: {json.dumps(new_conditions)}"
        query = "Adapt the current schedule to accommodate these new conditions while maintaining efficiency."
        return self.process_query(query, context)
    
    def generate_schedule_report(self, time_period, completed_tasks, performance_metrics):
        """
        Generate comprehensive scheduling performance report
        """
        context = f"Time Period: {time_period}\nCompleted Tasks: {json.dumps(completed_tasks)}\nPerformance: {json.dumps(performance_metrics)}"
        query = "Generate a comprehensive report on scheduling performance, efficiency, and recommendations for improvement."
        return self.process_query(query, context)
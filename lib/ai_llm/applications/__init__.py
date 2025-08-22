"""
Predefined AI Applications for MicroPython AI/LLM Library
"""

from .base_application import BaseAIApplication
from .weather_analyzer import WeatherAnalyzer
from .motor_controller import MotorController
from .smart_home_controller import SmartHomeController
from .security_system import SecuritySystem
from .lighting_controller import LightingController
from .robot_navigator import RobotNavigator
from .task_scheduler import TaskScheduler

__all__ = [
    'BaseAIApplication',
    'WeatherAnalyzer',
    'MotorController',
    'SmartHomeController',
    'SecuritySystem',
    'LightingController',
    'RobotNavigator',
    'TaskScheduler'
]
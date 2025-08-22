"""
MicroPython AI/LLM Library
A lightweight library for interacting with AI/LLM APIs on MicroPython devices
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .client import AIClient
from .models import ChatMessage, ChatResponse, ModelConfig
from .utils import format_prompt, validate_response

__all__ = [
    'AIClient',
    'ChatMessage', 
    'ChatResponse',
    'ModelConfig',
    'format_prompt',
    'validate_response'
]
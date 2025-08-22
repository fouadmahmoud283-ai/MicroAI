# 🧠 MicroAI

<div align="center">

**Intelligent MicroPython Library for AI-Powered IoT & Robotics**

[![MicroPython](https://img.shields.io/badge/MicroPython-1.20+-blue.svg)](https://micropython.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](https://github.com/fouadmahmoud281/MicroAI)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

*Transform your ESP32/ESP8266 into an intelligent IoT powerhouse with natural language processing*

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🎯 Examples](#-examples) • [🤝 Contributing](#-contributing)

</div>

---

## ✨ What is MicroAI?

**MicroAI** is a comprehensive MicroPython library that brings the power of Large Language Models (LLMs) and AI directly to your microcontroller projects. Whether you're building smart homes, autonomous robots, or intelligent IoT devices, MicroAI provides the tools you need to create truly intelligent embedded systems.

### 🎯 Key Highlights

> 🏠 **Smart Home Ready** - Control your entire home with natural language  
> 🤖 **Robotics Optimized** - Advanced navigation and task scheduling  
> 🌱 **IoT Focused** - Perfect for sensors, automation, and monitoring  
> ⚡ **Memory Efficient** - Designed specifically for microcontroller constraints  
> 🔌 **Plug & Play** - Easy integration with existing MicroPython projects

---

## 🌟 Features

<table>
<tr>
<td width="50%">

### 🧠 Core AI Features
- **🗣️ Natural Language Processing** - Chat with your devices
- **🔄 Multiple AI Providers** - OpenAI, custom endpoints
- **⚙️ Configurable Models** - Fine-tune for your needs
- **💾 Memory Optimized** - Works on ESP32/ESP8266
- **🛡️ Error Handling** - Robust and reliable
- **📚 Conversation History** - Context-aware interactions

</td>
<td width="50%">

### 🎯 Specialized Applications
- **🏠 Smart Home Controller** - Voice-controlled automation
- **🔒 Security System** - AI-powered threat detection  
- **💡 Lighting Controller** - Circadian & mood lighting
- **🤖 Robot Navigator** - Intelligent pathfinding
- **📅 Task Scheduler** - Smart task automation
- **🌤️ Weather Analyzer** - Sensor data intelligence
- **⚙️ Motor Controller** - Natural language motor control

</td>
</tr>
</table>

---

## 📁 Project Architecture

```
MicroAI/
├── 📂 lib/
│   └── 📂 ai_llm/
│       ├── 📄 __init__.py              # Main library exports
│       ├── 🔧 client.py                # Core AI client
│       ├── 📊 models.py                # Data models & structures
│       ├── 🛠️ utils.py                 # Utility functions
│       └── 📂 applications/            # Specialized AI apps
│           ├── 📄 __init__.py
│           ├── 🏗️ base_application.py  # Base class
│           ├── 🏠 smart_home_controller.py
│           ├── 🔒 security_system.py
│           ├── 💡 lighting_controller.py
│           ├── 🤖 robot_navigator.py
│           ├── 📅 task_scheduler.py
│           ├── 🌤️ weather_analyzer.py
│           └── ⚙️ motor_controller.py
├── 📂 examples/                       # Ready-to-run examples
├── 📂 docs/                          # Comprehensive documentation
├── 🚀 main.py                        # Quick start example
└── 📋 requirements.txt               # Dependencies
```

---

## 🛠️ Installation

### Method 1: Quick Install (Recommended)
```python
# Install using MicroPython's package manager
import mip
mip.install("github:fouadmahmoud281/MicroAI")
```

### Method 2: Manual Installation
```bash
# Clone the repository
git clone https://github.com/fouadmahmoud281/MicroAI.git

# Copy to your MicroPython device
cp -r MicroAI/lib/ai_llm /your-device/lib/
```

### Method 3: Using upip
```python
import upip
upip.install('micropython-urequests')  # Required dependency
upip.install('micropython-microai')
```

---

## 🚀 Quick Start

### 💬 Basic AI Chat
```python
from ai_llm import AIClient, ModelConfig

# 🔧 Setup your AI client
client = AIClient(
    api_key="your-openai-api-key",
    model_config=ModelConfig(
        model_name="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=150
    )
)

# 🗣️ Start chatting with your device!
response = client.simple_chat("Hello! What can you help me with?")
print("🤖 AI Response:", response)
```

### 🏠 Smart Home Control
```python
from ai_llm import SmartHomeController

# 🏡 Create your smart home assistant
home_ai = SmartHomeController(ai_client=client)

# 🗣️ Control with natural language
commands = [
    "Turn on the living room lights at 70% brightness",
    "Set the thermostat to 22 degrees",
    "Lock all doors and arm the security system"
]

for command in commands:
    result = home_ai.process_home_command(command)
    print(f"✅ {command} → {result}")
```

### 🤖 Robot Navigation
```python
from ai_llm import RobotNavigator

# 🚀 Create intelligent robot navigator
robot = RobotNavigator(ai_client=client)

# 📍 Navigate with AI assistance
sensor_data = {
    "ultrasonic_front": 150,
    "ultrasonic_left": 80,
    "ultrasonic_right": 200,
    "battery_level": 85
}

result = robot.process_navigation_command(
    "Navigate to the kitchen while avoiding obstacles",
    sensor_data=sensor_data
)
print("🗺️ Navigation plan:", result)
```

---

## 🎯 Application Showcase

<details>
<summary><b>🏠 Smart Home Applications</b></summary>

### 🎛️ Smart Home Controller
- **🔌 Device Control**: Lights, climate, appliances, sensors
- **⚡ Energy Optimization**: AI-driven energy saving
- **🛡️ Safety First**: Built-in safety validation
- **🏘️ Multi-room**: Manage entire house layouts

### 🔒 Security System  
- **🎯 Threat Detection**: AI-powered security analysis
- **🚨 Multi-zone**: Entry, perimeter, interior monitoring
- **📢 Smart Alerts**: Context-aware notifications
- **🔐 Access Control**: Intelligent user management

### 💡 Lighting Controller
- **🌅 Circadian Rhythm**: Health-optimized lighting
- **🎭 Dynamic Scenes**: Activity-based configurations  
- **💚 Energy Smart**: Efficient brightness control
- **🗣️ Voice Control**: "Set romantic mood lighting"

</details>

<details>
<summary><b>🤖 Robotics Applications</b></summary>

### 🗺️ Robot Navigator
- **🎯 Path Planning**: Optimal route calculation
- **👁️ Sensor Fusion**: Ultrasonic, camera, LIDAR, IMU
- **🛡️ Safety First**: Collision avoidance built-in
- **🗺️ SLAM Ready**: Mapping and localization support

### 📅 Task Scheduler
- **🧠 Smart Priority**: AI-driven task management
- **⚡ Resource Optimization**: Efficient allocation
- **🔄 Adaptive**: Real-time schedule adjustments
- **⚖️ Conflict Resolution**: Automatic conflict handling

</details>

<details>
<summary><b>🌍 Environmental Applications</b></summary>

### 🌤️ Weather Analyzer
- **📡 Multi-sensor**: Temperature, humidity, pressure, wind
- **💡 Smart Recommendations**: Irrigation, HVAC, activities
- **⚠️ Alert System**: Weather warnings & extreme conditions
- **🌱 Agricultural**: Crop and greenhouse optimization

### ⚙️ Motor Controller
- **🗣️ Natural Language**: "Turn motor 1 clockwise at 50%"
- **🛡️ Safety Validation**: Speed and angle limits
- **🔄 Multi-motor**: Coordinate multiple motors
- **📊 JSON Responses**: Structured command output

</details>

---

## 🎨 Configuration & Setup

### 📶 WiFi Configuration
```python
def setup_wifi(ssid: str, password: str):
    """🔗 Connect to WiFi network"""
    import network
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('🔍 Connecting to network...')
        wlan.connect(ssid, password)
        
        while not wlan.isconnected():
            pass
            
    print('✅ Network connected!')
    print('📡 Network config:', wlan.ifconfig())
```

### 🔧 API Configuration Options
```python
# 🔑 OpenAI Configuration
client = AIClient(
    api_key="sk-your-openai-key",
    base_url="https://api.openai.com/v1"
)

# 🏗️ Custom API Configuration  
client = AIClient(
    api_key="your-custom-key",
    base_url="https://your-api-endpoint.com/v1"
)

# ⚙️ Advanced Model Configuration
config = ModelConfig(
    model_name="gpt-4",
    max_tokens=200,
    temperature=0.8,
    top_p=0.9,
    frequency_penalty=0.1
)
```

---

## 📚 Examples & Demos

<table>
<tr>
<td align="center" width="33%">

### 💬 Basic Chat
**`examples/basic_chat.py`**

Simple AI conversation interface with your microcontroller

[View Example →](examples/basic_chat.py)

</td>
<td align="center" width="33%">

### 🏠 Smart Home Demo  
**`examples/smart_home_demo.py`**

Complete home automation with voice control

[View Example →](examples/smart_home_demo.py)

</td>
<td align="center" width="33%">

### 🤖 Robotics Demo
**`examples/robotics_demo.py`** 

Robot navigation and intelligent task scheduling

[View Example →](examples/robotics_demo.py)

</td>
</tr>
<tr>
<td align="center">

### 🌤️ Weather Analysis
**`examples/weather_analysis.py`**

Environmental sensor data analysis and recommendations

[View Example →](examples/weather_analysis.py)

</td>
<td align="center">

### ⚙️ Motor Control
**`examples/motor_control.py`**

Natural language motor control with safety validation

[View Example →](examples/motor_control.py)

</td>
<td align="center">

### 🌊 Streaming Responses
**`examples/streaming_response.py`**

Real-time AI response streaming for interactive applications

[View Example →](examples/streaming_response.py)

</td>
</tr>
</table>

---

## 🔧 Advanced Usage

### 🏗️ Create Custom AI Applications

Extend the `BaseAIApplication` class to build your own specialized AI applications:

```python
from ai_llm.applications import BaseAIApplication

class WeatherStationAI(BaseAIApplication):
    """🌡️ Custom weather station with AI analysis"""
    
    def get_default_system_prompt(self):
        return """
        You are a weather station AI assistant. Analyze environmental 
        data and provide actionable insights for optimal conditions.
        """
    
    def analyze_conditions(self, sensor_data: dict):
        prompt = f"""
        Current conditions: {sensor_data}
        
        Provide:
        1. Current weather summary
        2. Recommendations for outdoor activities  
        3. Any weather alerts or warnings
        """
        
        return self.process_query(prompt)
```

### ⚡ Performance Optimization

```python
# 💾 Memory management
import gc

def optimize_memory():
    """🔧 Optimize memory usage for long-running applications"""
    gc.collect()  # Force garbage collection
    print(f"💾 Free memory: {gc.mem_free()} bytes")

# 🔄 Conversation history management
client.clear_history()  # Clear old conversations
client.set_max_history(5)  # Limit conversation history
```

### 🛡️ Safety & Security Features

```python
# 🔒 Enable safety validation
home_controller = SmartHomeController(
    ai_client=client,
    safety_mode=True,  # Enable safety checks
    require_confirmation=True  # Require confirmation for critical actions
)

# ⚠️ Set operational limits
motor_controller = MotorController(
    ai_client=client,
    max_speed=50,  # Maximum motor speed (%)
    safety_timeout=30  # Emergency stop timeout (seconds)
)
```

---

## 🔍 API Reference

<details>
<summary><b>📚 Core Classes</b></summary>

### 🤖 AIClient
The main interface for AI API communication.

```python
class AIClient:
    def __init__(self, api_key: str, base_url: str = None, model_config: ModelConfig = None)
    def simple_chat(self, message: str) -> str
    def chat_completion(self, messages: List[ChatMessage]) -> ChatResponse
    def clear_history(self) -> None
```

### 💬 ChatMessage & ChatResponse
Message structures for AI conversations.

```python
@dataclass
class ChatMessage:
    role: str  # "user", "assistant", "system"
    content: str
    timestamp: float

@dataclass  
class ChatResponse:
    message: str
    tokens_used: int
    model: str
    finish_reason: str
```

</details>

<details>
<summary><b>🏠 Application Classes</b></summary>

### Smart Home Controller
```python
class SmartHomeController(BaseAIApplication):
    def process_home_command(self, command: str) -> dict
    def get_device_status(self, device_name: str) -> dict
    def set_safety_mode(self, enabled: bool) -> None
```

### Security System
```python
class SecuritySystem(BaseAIApplication):
    def analyze_security_event(self, event_data: dict) -> dict
    def process_alert(self, alert_type: str, details: dict) -> dict
    def get_threat_level(self) -> str
```

</details>

---

## 🚨 Troubleshooting

<details>
<summary><b>💾 Memory Issues</b></summary>

**Problem**: `MemoryError` or system crashes
**Solutions**:
- ✅ Reduce `max_tokens` in ModelConfig (try 100-150)
- ✅ Clear conversation history regularly: `client.clear_history()`
- ✅ Use `gc.collect()` after AI operations
- ✅ Limit concurrent AI requests

```python
# 🔧 Memory-optimized configuration
config = ModelConfig(
    model_name="gpt-3.5-turbo",
    max_tokens=100,  # Reduced for memory efficiency
    temperature=0.7
)
```

</details>

<details>
<summary><b>🌐 Network Issues</b></summary>

**Problem**: Connection timeouts or network errors
**Solutions**:
- ✅ Check WiFi signal strength
- ✅ Verify API endpoint accessibility  
- ✅ Implement retry logic with exponential backoff
- ✅ Monitor API rate limits

```python
# 🔄 Retry mechanism example
import time

def retry_request(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(2 ** attempt)  # Exponential backoff
```

</details>

<details>
<summary><b>🔑 API Issues</b></summary>

**Problem**: Authentication or API errors
**Solutions**:
- ✅ Verify API key validity and permissions
- ✅ Check API endpoint URL format
- ✅ Monitor usage quotas and billing
- ✅ Test with minimal requests first

</details>

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help make MicroAI even better:

### 🌟 Ways to Contribute
- 🐛 **Bug Reports** - Found an issue? Let us know!
- 💡 **Feature Requests** - Have an idea? We'd love to hear it!
- 📝 **Documentation** - Help improve our guides and examples
- 🔧 **Code Contributions** - Submit pull requests for new features
- 🧪 **Testing** - Help test on different hardware platforms

### 🚀 Development Setup
```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/your-username/MicroAI.git
cd MicroAI

# 3. Create a feature branch
git checkout -b feature/amazing-new-feature

# 4. Make your changes and commit
git commit -am "Add amazing new feature"

# 5. Push and create a Pull Request
git push origin feature/amazing-new-feature
```

### 📋 Contribution Guidelines
- ✅ Follow existing code style and conventions
- ✅ Add tests for new functionality
- ✅ Update documentation as needed
- ✅ Ensure backwards compatibility
- ✅ Test on real hardware when possible

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Open Source, Free to Use
✅ Commercial use    ✅ Modification    ✅ Distribution    ✅ Private use
```

---

## 🙏 Acknowledgments

<table>
<tr>
<td align="center" width="25%">

### 🐍 MicroPython
For providing an amazing Python implementation for microcontrollers

</td>
<td align="center" width="25%">

### 🤖 OpenAI  
For making powerful AI accessible through their APIs

</td>
<td align="center" width="25%">

### 🌐 Open Source
The amazing open source community that makes projects like this possible

</td>
<td align="center" width="25%">

### 🧪 Contributors
All the developers and testers who help improve MicroAI

</td>
</tr>
</table>

---

## 📞 Support & Community

<div align="center">

### 💬 Get Help & Connect

[![GitHub Issues](https://img.shields.io/github/issues/fouadmahmoud281/MicroAI.svg)](https://github.com/fouadmahmoud281/MicroAI/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/fouadmahmoud281/MicroAI.svg)](https://github.com/fouadmahmoud281/MicroAI/discussions)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](docs/)

**📧 Contact**: [fouad.mahmoud281@example.com](mailto:fouad.mahmoud281@example.com)  
**🐛 Bug Reports**: [Create an Issue](https://github.com/fouadmahmoud281/MicroAI/issues/new)  
**💡 Feature Requests**: [Start a Discussion](https://github.com/fouadmahmoud281/MicroAI/discussions/new)  
**📖 Documentation**: [View Full Docs](docs/API.md)

</div>

---

<div align="center">

### 🚀 Ready to Build the Future?

**MicroAI transforms your ideas into intelligent reality**

[Get Started Now](#-installation) • [View Examples](#-examples) • [Read the Docs](#-api-reference)

---

**Made with ❤️ by [Fouad Mahmoud](https://github.com/fouadmahmoud281) for the MicroPython & IoT Community**

⭐ **If MicroAI helped your project, please consider giving it a star!** ⭐

</div>
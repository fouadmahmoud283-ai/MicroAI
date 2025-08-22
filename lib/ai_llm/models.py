class ChatMessage:
    """
    Represents a chat message
    """
    
    def __init__(self, role, content, name=None):
        self.role = role  # "system", "user", "assistant"
        self.content = content
        self.name = name
    
    def to_dict(self):
        msg_dict = {
            "role": self.role,
            "content": self.content
        }
        if self.name:
            msg_dict["name"] = self.name
        return msg_dict
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            role=data.get("role"),
            content=data.get("content"),
            name=data.get("name")
        )

class ChatChoice:
    """
    Represents a chat completion choice
    """
    
    def __init__(self, index, message, finish_reason=None):
        self.index = index
        self.message = message
        self.finish_reason = finish_reason
    
    @classmethod
    def from_api_data(cls, data):
        message = ChatMessage.from_dict(data.get("message", {}))
        return cls(
            index=data.get("index"),
            message=message,
            finish_reason=data.get("finish_reason")
        )

class ChatResponse:
    """
    Represents a chat completion response
    """
    
    def __init__(self, id, object_type, created, model, choices, usage=None):
        self.id = id
        self.object = object_type
        self.created = created
        self.model = model
        self.choices = choices
        self.usage = usage
    
    @classmethod
    def from_api_response(cls, data):
        choices = [ChatChoice.from_api_data(choice) for choice in data.get("choices", [])]
        return cls(
            id=data.get("id"),
            object_type=data.get("object"),
            created=data.get("created"),
            model=data.get("model"),
            choices=choices,
            usage=data.get("usage")
        )

class ModelConfig:
    """
    Configuration for AI model parameters
    """
    
    def __init__(self, model_name="gpt-3.5-turbo", max_tokens=150, temperature=0.7, top_p=1.0):
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
    
    def to_dict(self):
        return {
            "model": self.model_name,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_p": self.top_p
        }
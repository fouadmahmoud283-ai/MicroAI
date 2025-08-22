import ujson as json
import re

def format_prompt(template, **kwargs):
    """
    Format a prompt template with given parameters
    
    Args:
        template: String template with {variable} placeholders
        **kwargs: Variables to substitute
        
    Returns:
        Formatted string
    """
    try:
        return template.format(**kwargs)
    except KeyError as e:
        print(f"Missing template variable: {e}")
        return template

def validate_response(response_text):
    """
    Validate and clean AI response
    
    Args:
        response_text: Raw response text
        
    Returns:
        Cleaned response text
    """
    if not response_text:
        return ""
    
    # Remove excessive whitespace
    cleaned = re.sub(r'\s+', ' ', response_text.strip())
    
    # Remove common AI prefixes
    prefixes_to_remove = [
        "AI: ", "Assistant: ", "Bot: ", "Response: "
    ]
    
    for prefix in prefixes_to_remove:
        if cleaned.startswith(prefix):
            cleaned = cleaned[len(prefix):]
            break
    
    return cleaned

def chunk_text(text, max_length=1000):
    """
    Split text into chunks for processing
    
    Args:
        text: Text to chunk
        max_length: Maximum chunk length
        
    Returns:
        List of text chunks
    """
    if len(text) <= max_length:
        return [text]
    
    chunks = []
    words = text.split()
    current_chunk = []
    current_length = 0
    
    for word in words:
        word_length = len(word) + 1  # +1 for space
        
        if current_length + word_length > max_length:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
            else:
                # Single word longer than max_length
                chunks.append(word)
                current_length = 0
        else:
            current_chunk.append(word)
            current_length += word_length
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def safe_json_loads(json_string):
    """
    Safely load JSON with error handling
    
    Args:
        json_string: JSON string to parse
        
    Returns:
        Parsed object or None if error
    """
    try:
        return json.loads(json_string)
    except (ValueError, TypeError) as e:
        print(f"JSON parsing error: {e}")
        return None
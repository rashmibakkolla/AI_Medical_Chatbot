import os
import base64
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment.")

def encode_image(image_path: str) -> str:
    """Encode an image to a base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_with_query(query: str, model: str, encoded_image: str, api_key: str = None) -> str:
    """Send an image + query to the GROQ model and return its reply."""
    api_key = api_key or GROQ_API_KEY
    if not api_key:
        raise ValueError("GROQ_API_KEY is required.")
    client = Groq(api_key=api_key)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ]
        }
    ]
    chat_completion = client.chat.completions.create(messages=messages, model=model)
    return chat_completion.choices[0].message.content

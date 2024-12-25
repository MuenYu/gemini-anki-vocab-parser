from utils import *
from google import genai
from google.genai import types

client = genai.Client(api_key=read_line_from_txt("key.txt"))

# Create the model
generation_config = types.GenerateContentConfig(
    temperature=1.1,
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192,
    response_mime_type="application/json",
    response_schema={
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "front": {
                    "type": "string"
                },
                "definition": {
                    "type": "string"
                },
                "cn-definition": {
                    "type": "string"
                },
                "example": {
                    "type": "string"
                },
                "cn-example": {
                    "type": "string"
                }
            }
        }
    }
)


def ask_gemini(prompt):
    """
    send request to gemini
    :param prompt: model request
    :return: return from gemini
    """
    return client.models.generate_content(model='gemini-exp-1206', contents=prompt, config=generation_config)

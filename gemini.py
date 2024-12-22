from utils import *
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

key = read_line_from_txt("key.txt")
genai.configure(api_key=key)

# Create the model
generation_config = GenerationConfig(
    temperature=1,
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192,
    # response_mime_type="text/plain",
    response_mime_type="application/json",
    response_schema={
        "type": "object",
        "properties": {
            "response": {
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
        }
    }
)

model = genai.GenerativeModel(
    model_name="gemini-exp-1206",
    generation_config=generation_config,
)

chat_session = model.start_chat()


def ask_gemini(prompt):
    """
    send request to gemini
    :param prompt: model request
    :return: return from gemini
    """
    return chat_session.send_message(prompt)

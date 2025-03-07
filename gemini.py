from utils import *
from google import genai

client = genai.Client(api_key=read_line_from_txt("key.txt"))

def ask_gemini(config, prompt):
    """
    send request to gemini
    :param config: model config
    :param prompt: model request
    :return: return from gemini
    """
    return client.models.generate_content(model='gemini-2.0-flash', contents=prompt, config=config)

import json

from google.genai import types

from gemini import ask_gemini
from utils import export_csv

prompt = """
I am an intermediate level English learner (B1-B2 level), and I want to improve my vocabulary.
I will provide you with a vocabulary lists, and you need to explain these words in both English and Chinese ways.
Your explanation should be concise and easy to grasp, considering my English skill.

There are three properties per entry: front, definition and cn-definition

- front: the vocab
- definition: part of speech and its explanation in your own words. If multiple meaning available, list them all by frequency
- cn-definition: It's not necessary to be the translation of definition, just explain in the most straight way
- example: a simple sentence to demonstrate the correct usage of `front`
- cn-example: the Chinese translation of example 

Here's an example, genital:

    "front": "genital",
    "definition": "n. the organ to have sex\nadj. relating to the organs of reproduction",
    "cn-definition": "n. 生殖器官\nadj. 生殖器的"
    "example"： "Men and women have different genitals"
    "cn-example"： "男性和女性有不同的生殖器"

Don't miss any properties for any entry!
Now you need to do the job for the vocab list below:

"""

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
header = ['front', 'definition', 'cn-definition', 'example', 'cn-example']


def gen_anki_cards(words, batch_size, output):
    for i in range(0, len(words), batch_size):
        batch = words[i:i + batch_size]
        batch_prompt = f'{prompt}{batch}'
        resp = ask_gemini(generation_config, batch_prompt).text
        parsed_response = json.loads(resp)
        if len(batch) == len(parsed_response):
            export_csv(header, parsed_response, output)
            print(f'log: words {i + 1} to {i + len(batch)} are done!')
        else:
            print(f"return from gemini: {parsed_response}")
            print(f"expected counts: {len(words)}, actual counts: {len(parsed_response)}")
            print("gemini: data is not integrated")
            exit(1)
    print("Complete!")
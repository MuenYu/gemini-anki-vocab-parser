from google.genai import types

from gemini import ask_gemini
from utils import export_csv

prompt = """
I am an intermediate level English learner (B1-B2 level), and I want to improve my vocabulary.
I will provide you with a vocabulary lists, and you need to use these words to make a short story.
The story should be concise and easy to grasp, considering my English skill.
The story length should be shorter than 5 times of the length of vocabulary list

For each word in the list, you need to demonstrate its part of speech and Chinese meaning in a pair of bracket.

e.g. Her smile is so healing(adj. 治愈的).

Now you need to do the job for the vocab list below:
"""

# Create the model
generation_config = types.GenerateContentConfig(
    temperature=1.1,
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192,
    response_mime_type="text/plain",
)

header = ['story']


def gen_story(words, batch_size, output):
    for i in range(0, len(words), batch_size):
        batch = words[i:i + batch_size]
        batch_prompt = f'{prompt}{batch}'
        data = ask_gemini(generation_config, batch_prompt).text
        export_csv(header, data, output)
        print(f'log: words {i + 1} to {i + len(batch)} are done!')

    print("Complete!")

import json

from gemini import *
from utils import *

source = './source.txt'
output = './output.csv'
words = read_lines_from_txt(source)
prompt = f"""
I am an intermediate level English learner (B1-B2 level), and I want to improve my vocabulary.
I will provide you with a vocabulary lists, and you need to explain these words in both English and Chinese ways.
Your explanation should be concise and easy to grasp, considering my English skill.

There are three properties per entry: front, definition and cn-definition

- front: the vocab
- definition: part of speech and its explanation. If multiple meaning available, list them all by frequency
- cn-definition: It's not necessary to be the translation of definition, just explain in the most straight way

Here's an example, genital:

    "front": "genital",
    "definition": "n. the organ to have sex\nadj. relating to the organs of reproduction",
    "cn-definition": "n. 生殖器官\nadj. 生殖器的"

Don't miss any properties for any entry!
Now you need to do the job for the vocab list below:

{words}
"""

if __name__ == "__main__":
    data = json.loads(ask_gemini(prompt).text)
    export_csv(data, output)
    print("Complete!")

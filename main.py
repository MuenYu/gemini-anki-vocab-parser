from anki import gen_anki_cards
from story import gen_story
from utils import *

source = './source.txt'
output = './output.csv'
words = read_lines_from_txt(source)

batch_size = 20
is_card_mode = True

if __name__ == "__main__":
    if is_card_mode:
        gen_anki_cards(words,batch_size,output)
    else:
        gen_story(words, batch_size, output)

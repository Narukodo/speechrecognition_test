import os
from pathlib import Path
import string


texts_directory = Path(__file__).parent / 'readings'
texts = {}
for text_file in texts_directory.iterdir():
    text = text_file.read_text()
    text.strip(string.punctuation)
    text.replace('\n', ' ')
    text_filename = text_file.name.replace('.txt', '')
    texts[text_filename] = text.lower()

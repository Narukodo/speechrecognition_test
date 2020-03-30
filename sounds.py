import speech_recognition as sr
from pathlib import Path 
import os
import re


sound_folder = Path().cwd() / 'sounds/samples'
text_names = [text_name for text_name in os.listdir(sound_folder) if os.path.isdir(sound_folder / text_name)]
for text_name in text_names:
    sound_file_names = [(text_name, file_name) for file_name in os.listdir(sound_folder / text_name) if re.match(r'^.+\.wav$', file_name)]
    
sound_files = [(text_name, os.path.join(os.path.dirname(os.path.realpath(__file__)), f'sounds/samples/{text_name}/{sound_file}')) for (text_name, sound_file) in sound_file_names]
r = sr.Recognizer()
trial_sounds = []
for (text_name, sound_file) in sound_files:
    with sr.AudioFile(sound_file) as source:
        trial_sounds.append((text_name, r.record(source)))
# sound_file_names = [f for f in sound_folder.glob('**/*') if f.is_file()]

import speech_recognition as sr
from pathlib import Path 
import os

sound_folder = Path().cwd() / 'sounds/samples'
sound_file_names = os.listdir(sound_folder)
sound_files = [os.path.join(os.path.dirname(os.path.realpath(__file__)), f'sounds/samples/{sound_file}') for sound_file in sound_file_names]
r = sr.Recognizer()
trial_sounds = []
for sound_file in sound_files:
    with sr.AudioFile(sound_file) as source:
        trial_sounds.append(r.record(source))
# sound_file_names = [f for f in sound_folder.glob('**/*') if f.is_file()]

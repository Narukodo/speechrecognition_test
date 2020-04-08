from collections import namedtuple
import speech_recognition as sr
from pathlib import Path 
import os
import re

WavInfo = namedtuple('WavInfo', ['filename', 'label', 'sound_bytes'])

sound_samples_folder = Path().cwd() / 'sounds/samples'
# indicate which text to compare speech to
speech_labels = [folder_name for folder_name in os.listdir(sound_samples_folder) if os.path.isdir(sound_samples_folder / folder_name)]
wav_filenames = []
for speech_label in speech_labels:
    curfolder_wavfiles = [(speech_label, wav_filename) for wav_filename in os.listdir(sound_samples_folder / speech_label) if re.match(r'^.+\.wav$', wav_filename)]
    wav_filenames = wav_filenames + curfolder_wavfiles

wav_filedata = [(wav_filename, speech_label, os.path.join(os.path.dirname(os.path.realpath(__file__)), f'sounds/samples/{speech_label}/{wav_filename}')) for (speech_label, wav_filename) in wav_filenames]
r = sr.Recognizer()
trial_sounds = []
for (wav_filename, speech_label, wav_filepath) in wav_filedata:
    with sr.AudioFile(wav_filepath) as source:
        trial_sounds.append(WavInfo(wav_filename, speech_label, r.record(source)))

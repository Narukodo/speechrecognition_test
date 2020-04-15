from collections import namedtuple
import speech_recognition as sr
from speech_recognition import AudioData
import os
from pathlib import Path 
import re

r = sr.Recognizer()

WavInfo = namedtuple('WavInfo', ['filename', 'label', 'sound_bytes', 'uri'])

def convert_to_audiofile(filepath):
    with sr.AudioFile(filepath) as source:
        return r.record(source)

def initialize():
    # The name for the new bucket
    bucket_name = "test_speech_rec_bucket"
    trial_sounds = set()
    sound_sample_folder = Path('sound_samples/samples')
    labels = [label for label in os.listdir(sound_sample_folder) if os.path.isdir(sound_sample_folder / label)]
    for label in labels:
        wav_files = [filename for filename in os.listdir(sound_sample_folder / label) if re.match(r'.*?\.wav$', filename)]
        for wav_filename in wav_files:
            recording = convert_to_audiofile(os.path.realpath(sound_sample_folder / label / wav_filename))
            trial_sounds.add(WavInfo(wav_filename, label, sound_bytes=recording, uri=f'gs://{bucket_name}/{label}/{wav_filename}'))
    return trial_sounds

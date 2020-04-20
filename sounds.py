from dataclasses import dataclass
import speech_recognition as sr
from speech_recognition import AudioData
import os
from pathlib import Path
import re

r = sr.Recognizer()


@dataclass
class WavInfo:
    filename: str
    label: str
    sound_bytes: AudioData = None
    uri: str = None


def convert_to_audiofile(filepath):
    with sr.AudioFile(filepath) as source:
        return r.record(source)


def initialize():
    # The name for the new bucket
    bucket_name = "test_speech_rec_bucket"
    trial_sounds = []
    sound_sample_folder = Path('sound_samples/samples')
    labels = [sub_dir.name for sub_dir in sound_sample_folder.iterdir() if sub_dir.is_dir()]
    for label in labels:
        wav_files = [filename for filename in os.listdir(sound_sample_folder / label) if re.match(r'.*?\.wav$', filename)]
        for wav_filename in wav_files:
            recording = convert_to_audiofile(os.path.realpath(sound_sample_folder / label / wav_filename))
            trial_sounds.append(WavInfo(wav_filename, label, sound_bytes=recording, uri=f'gs://{bucket_name}/{label}/{wav_filename}'))
    return trial_sounds

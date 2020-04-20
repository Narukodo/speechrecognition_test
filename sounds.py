from dataclasses import dataclass
from dotenv import load_dotenv
from google.cloud import storage
import speech_recognition as sr
from speech_recognition import AudioData
import os
from pathlib import Path
import re
# Imports the Google Cloud client library
# from sounds import WavInfo

r = sr.Recognizer()


@dataclass
class WavInfo:
    filename: str
    label: str
    sound_bytes: AudioData = None
    uri: str = None


def convert_to_audiofile(filepath):
    with sr.AudioFile(filepath) as source:
        return source


def initialize():
    load_dotenv()

    # Instantiates a client
    storage_client = storage.Client()

    # The name for the new bucket
    bucket_name = "test_speech_rec_bucket"

    speech_bucket = storage_client.get_bucket(bucket_name)
    all_files = [blob for blob in list(speech_bucket.list_blobs()) if re.match(r'.*\/.*\.wav', blob.name)]
    trial_sounds = []
    for blob in all_files:
        (sound_label, filename) = blob.name.split('/')
        sounds_folder = Path(f'sounds/samples/{sound_label}')
        # GCS and local storage assumed to be in sync
        # The two need to be in sync for data collection purposes, however if need arises, a guard will be put in place
        wav_filepath = os.path.realpath(sounds_folder / filename)
        # with sr.AudioFile(wav_filepath) as source:
        source = convert_to_audiofile(wav_filepath)
        trial_sounds.append(WavInfo(filename, sound_label, sound_bytes=r.record(source), uri=f'gs://{blob.bucket.name}/{blob.name}'))
    return trial_sounds

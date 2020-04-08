from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from gcs_read import trial_sounds
import speech_recognition as sr
import io
import os
import requests

r = sr.Recognizer()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './google-cloud-credentials.json'

# storage_uri pulled from gcs_read
# completely disregarding uploading a file to cloud first
def sample_long_running_recognize(storage_uri):
    client = speech_v1.SpeechClient()

    # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = "en-US"

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "encoding": encoding,
        "audio_channel_count": 2
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    response = operation.result()

    transcripts = []
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        transcripts.append(alternative.transcript)
    print(' '.join(transcripts))

# sample_long_running_recognize(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sounds/samples/philippians/philippians.wav'))
for sound in trial_sounds:
    sample_long_running_recognize(sound.uri)
# sample_long_running_recognize('gs://test_speech_rec_bucket/Overview Philippians.wav')
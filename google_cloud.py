from google.api_core.exceptions import GoogleAPICallError
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import speech_recognition as sr
import os

r = sr.Recognizer()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './google-cloud-credentials.json'


# completely disregarding uploading a file to cloud first
def sample_long_running_recognize(storage_uri):
    client = speech_v1.SpeechClient()

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

    try:
        operation = client.long_running_recognize(config, audio)
    except GoogleAPICallError as err:
        print(f'Problem occurred with {storage_uri}:\n', err)

    response = operation.result()

    transcripts = []
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        transcripts.append(alternative.transcript)
    return ' '.join(transcripts)

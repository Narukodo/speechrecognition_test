import abc
from abc import ABC
# from ibm_watson import SpeechToTextV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# import os
# import requests

import json
import os
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# class WatsonEngine(SpeechEngine):
#     def __init__(self):
#         self.id = os.getenv('WATSON_ID')
#         self.key = os.getenv('WATSON_KEY')
#         self.authenticator = IAMAuthenticator(self.key)
    
#     def recognize(self, audio_data):
#         raw_data = audio_data.get_raw_data(convert_rate=1600, convert_width=2)
#         flac_data = audio_data.get_flac_data(
#             convert_rate=None if audio_data.sample_rate >= 16000 else 16000,  # audio samples should be at least 16 kHz
#             convert_width=None if audio_data.sample_width >= 2 else 2  # audio samples should be at least 16-bit
#         )
#         speech_to_text = SpeechToTextV1(authenticator=authenticator)
#         requests.post(auth=('apikey', '{self.key}\n--header'))
#         speech_to_text.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com')

class SpeechEngine(ABC):
    @abc.abstractmethod
    def recognize(self, audio_data):
        pass

apikey = os.getenv('WATSON_KEY')
url = os.getenv('WATSON_URL')

authenticator = IAMAuthenticator(f'{apikey}')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url(f'{url}')

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

class WatsonEngine(SpeechEngine):
    def recognize(self, audio_data):
        flac_data = AudioSource(audio_data.get_flac_data())
        speech_to_text.recognize_using_websocket(
            audio=flac_data,
            content_type='audio/flac',
            recognize_callback=myRecognizeCallback,
            model='en-US_BroadbandModel',
            keywords=['colorado', 'tornado', 'tornadoes'],
            keywords_threshold=0.5,
            max_alternatives=3)

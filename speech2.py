#!/usr/bin/env python3

import speech_recognition as sr
from pathlib import Path
from os import path
from experiment.experiment import Experiment
from sounds import trial_sounds

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "sounds/samples/clearspeech.wav")
exp = Experiment()

# use the audio file as the audio source
r = sr.Recognizer()
# with open(AUDIO_FILE) as source:
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# # recognize speech using Sphinx
try:
    # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    audio_text = r.recognize_sphinx(audio)
    print(exp.run_experiment(r.recognize_sphinx))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# # recognize speech using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# WIT_AI_KEY = "KDQ4NM7SLFJBP7CVBN6L2WWDGOT432Z2"  # Wit.ai keys are 32-character uppercase alphanumeric strings
# try:
#     print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
# except sr.UnknownValueError:
#     print("Wit.ai could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Houndify
# HOUNDIFY_CLIENT_ID = "DOxS1E157czbiv8nIH3Njw=="  # Houndify client IDs are Base64-encoded strings
# HOUNDIFY_CLIENT_KEY = "a4zo9uTFB19oCE3sOD8X9O4O5vAqczJUzTmdcyrI3E9QVLic_K9lMu-MsnWZ-SJfHykYtfJfNgjN4Bt-8hQLrg=="  # Houndify client keys are Base64-encoded strings
# try:
#     print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
# except sr.UnknownValueError:
#     print("Houndify could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
# IBM_USERNAME = "e2003bf3-1f45-41a2-ac66-0d18e6f2a817"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
# IBM_PASSWORD = "W3lBac8wizZOAHaTlkMS3izIxPstnCRiq5lGARlME_0Z"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
# try:
#     print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
# except sr.UnknownValueError:
#     print("IBM Speech to Text could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from IBM Speech to Text service; {0}".format(e))

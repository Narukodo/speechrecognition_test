#!/usr/bin/env python3

import speech_recognition as sr
from pathlib import Path
from os import path
from experiment.experiment import Experiment
from sounds import trial_sounds

exp = Experiment()

# use the audio file as the audio source
r = sr.Recognizer()

# recognize speech using Sphinx
try:
    # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    exp.run_experiment('CMUSphinx', r.recognize_sphinx)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    exp.run_experiment('Google Speech Recognition', r.recognize_google)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


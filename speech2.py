#!/usr/bin/env python3

import speech_recognition as sr
from pathlib import Path
import json
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


import datetime
from collections import namedtuple

from experiment.spreadsheet import Spreadsheet

from sounds import initialize
import speech_recognition as sr
from texts.texts import texts as speeches

trial_sounds = sounds.initialize()

DataPoint = namedtuple('DataPoint', ['filename', 'wer'])

spreadsheet = Spreadsheet()

class Experiment:
    def run_experiment(self, engine_name, speech_to_text_fn, field):
        spreadsheet.add_speech_engine(engine_name)
        experiment_results = []
        for wav_info in trial_sounds:
            for i in range(5):
                experiment_results.append(self.trial(speech_to_text_fn, wav_info, field))
        spreadsheet.populate_table(engine_name, experiment_results)
        return experiment_results

    # trial: function, WavInfo --> DataPoint
    def trial(self, speech_to_text_fn, wav_info, field):
        filename = wav_info.filename
        label = wav_info.label
        sound_bytes = getattr(wav_info, field)
        start_time = datetime.datetime.now()
        try:
            guess = speech_to_text_fn(sound_bytes)  # will take in a file
        except sr.UnknownValueError:
            return DataPoint(filename, -1, -1, -1)
        end_time = datetime.datetime.now()
        latency = start_time - end_time
        return DataPoint(filename, self.calculate_accuracy(guess, label))

    def edit_distance(self, words1, words2):
        if len(words1) == 0:
            return len(words2)
        if len(words2) == 0:
            return len(words1)
        ed_calc = [[idx + idx2 for idx in range(len(words1) + 1)] for idx2 in range(len(words2) + 1)] # edit distance calculations
        
        for (idx2, word2) in enumerate(words2):
            for (idx1, word1) in enumerate(words1):
                if word1 == word2:
                    r = ed_calc[idx2][idx1]
                else:
                    r = ed_calc[idx2][idx1] + 1
                ed_calc[idx2 + 1][idx1 + 1] = min([ed_calc[idx2][idx1 + 1] + 1, ed_calc[idx2 + 1][idx1] + 1, r])
        return ed_calc[len(words2)][len(words1)]

    # calculating accuracy by (edit distance)/number of words
    def calculate_accuracy(self, guess, text_name):
        # Ensuring a difference in capitalization will not be counted as a different word
        guess_words = guess.lower().split(' ')
        actual_words = speeches[text_name].lower().split(' ')
        ed = self.edit_distance(guess_words, actual_words)
        return ed/len(actual_words)

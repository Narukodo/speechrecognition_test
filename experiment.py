import datetime

import sounds
import texts  # type: array

class Experiment:
    def trial(self, speech_to_text_fn):
        sound_trials = []
        for (idx, sound) in enumerate(sounds):
            start_time = datetime.datetime.now()
            guess = speech_to_text_fn(sounds)
            end_time = datetime.datetime.now()
            sound_trials.append((start_time, end_time, self.calculate_accuracy(guess, idx)))

    # calculating accuracy by (edit distance)/number of words
    def calculate_accuracy(self, guess, idx):
        guess_words = guess.split(' ')
        actual_words = texts[idx].split(' ')
        guess_idx = 0
        for (idx, actual_word) in enumerate(actual_words):
            if actual_word == guess_words[guess_idx]:
                guess_idx += 1

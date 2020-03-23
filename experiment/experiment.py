import datetime

from sounds import trial_sounds

text = 'please call stella ask her to bring these things with her from the store six spoons of fresh snow peas five thick slabs of blue cheese and maybe a snack for her brother bob we also need a small plastic snake and a big toy frog for the kids she can scoop these things into three red bags and we will go meet her wednesday at the train station'

class Experiment:
    def run_experiment(self, speech_to_text_fn):
        experiment_results = []
        for i in range(5):
            for sound in trial_sounds:
                experiment_results.append(self.trial(speech_to_text_fn, sound))
        return experiment_results

    def trial(self, speech_to_text_fn, sound):
        start_time = datetime.datetime.now()
        guess = speech_to_text_fn(sound)  # will take in a file
        end_time = datetime.datetime.now()
        return (start_time - end_time, self.calculate_accuracy(guess))

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
    def calculate_accuracy(self, guess):
        guess_words = guess.split(' ')
        actual_words = text.split(' ')
        ed = self.edit_distance(guess_words, actual_words)
        return ed/len(actual_words)

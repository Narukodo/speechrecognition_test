import datetime

from sounds import trial_sounds


text = 'please call stella ask her to bring these things with her from the store six spoons of fresh snow peas five thick slabs of blue cheese and maybe a snack for her brother bob we also need a small plastic snake and a big toy frog for the kids she can scoop these things into three red bags and we will go meet her wednesday at the train station'
text2 = 'ultimately the goal is to ease the guidelines and open things up to very large sections of our country as we near the end of our historic battle with the invisible enemy it’s been going for a while but we win we win i said earlier today that i hope we can do this by easter i think that would be a great thing for our country and we’re all working very hard to make that a reality we’ll be meeting with a lot of people to see if it can be done easter is a very special day for many reasons for me for a lot of a lot of our friends it’s a very special day and what a great timeline this would be easter is our timeline what a great timeline that would be my first priority is always the health and safety of the american people i want everyone to understand that we are continuing to evaluate the data I’m also hopeful to have americans working again by that easter that beautiful easter day but rest assured every decision we make is grounded solely in the health safety and wellbeing of our citizens this is a medical crisis this isn’t a financial crisis but it’s a uh a thing that nobody has seen for many many decades nothing like this'

speeches = {
    'stella': text,
    'trump': text2
}


class Experiment:
    def run_experiment(self, speech_to_text_fn):
        experiment_results = []
        for i in range(5):
            for sound_and_name in trial_sounds:
                experiment_results.append(self.trial(speech_to_text_fn, sound_and_name))
        return experiment_results

    def trial(self, speech_to_text_fn, sound_and_name):
        (name, sound) = sound_and_name
        start_time = datetime.datetime.now()
        guess = speech_to_text_fn(sound)  # will take in a file
        end_time = datetime.datetime.now()
        latency = start_time - end_time
        return (latency.secondsm , self.calculate_accuracy(guess, name))

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

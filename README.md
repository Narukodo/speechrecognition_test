# Speech Recognition
This project runs a few speech recognition engines against different kinds of speech with varying speeds, accents, and lengths, and compares and contrasts the performance of each of them.
The engines are tested against the following set of criteria:
1) Accuracy
2) Latency
3) Prices

These criteria is based on our company OKR to be first. Emphasis is placed on accuracy, following the philosophy that "bad data is worse than no data." There is no use being first at the wrong times or while executing the wrong course of action. If the engine cannot produce reliable results, then it would be better not to use it at all, regardless of how fast it can produce an output. Latency will also be taken into consideration however, as we cannot be first if we acquire accurate results after our competitors.

## Sources:
Speech data acquired from [Kaggle's speech accent archive](https://www.kaggle.com/rtatman/speech-accent-archive)
- Fast speech: armenian6.wav
- Slow speech: hungarian8.wav
- Thick accent: bambara4.wav
- Normal speech: serbian9.wav

## Engines
- IBM Watson
- Dialogflow
- CMUSphinx
- Google Speech Recognition
- Kaldi
- Houndify

These were some of the top engines suggested in various sources about which speech recognition engines to use. Some commonly known engines that focus more on natural language processing (NLP) have been disqualified because the length of speech they are willing to process is too short to be of any practical use for the purposes of gathering data.

## Assumptions
This project assumes that conversion from video to WAV or mp3 to WAV takes the same amount of time for all engines. Though whether the engine takes in MP3 files or other audio and video formats will be noted at the end of this report.
Contractions will be considered one word, not two.
Punctuation is not taken into consideration, but could be a plus and will be noted at the end of this report.
Not proessing the sound file because the engine cannot recognize it will count as an error on the whatever was not processed.
## Procedure
This project will be broken up into a series of smaller experiments testing for accuracy and latency above.
### Set-up
All engines will be set up to simply be fed the sound file. As most sound recognition engines seem to accept only WAV files, all MP3 files will be converted to WAV files beforehand.
### Accuracy
Trial procedure will consist of:
1) Feeding the sound file into the sound recognition engine
2) Recording the engine's guess and calculating the [WER](https://blog.voicebase.com/how-to-compare-speech-engine-accuracy) (using [this method](https://www.quora.com/How-do-I-measure-the-accuracy-of-speech-recognition))

### Latency
Trial procedure will consist of:
1) Feeding the sound file into the sound recognition engine
2) Recording when the engine was fed the sound file
3) Recording when the engine finishes processing the sound file

The latency will be compared against the original length of the sound file--comparing how fast the engine took to transcribe the audio file to how fast the speaker took to speak.

### Recordings
The results will be saved in a spreadsheet in the root directory of this project.

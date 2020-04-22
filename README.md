# Speech Recognition
This project runs a few speech recognition engines against different kinds of speech with varying speeds, accents, and lengths, and compares and contrasts the performance of each of them.
The engines are tested against the following set of criteria:
1) Accuracy
2) Latency

These criteria is based on our company OKR to be first. Emphasis is placed on accuracy, following the philosophy that "bad data is worse than no data." There is no use being first at the wrong times or while executing the wrong course of action. If the engine cannot produce reliable results, then it would be better not to use it at all, regardless of how fast it can produce an output.

## Sources:
Speech data acquired from [Kaggle's speech accent archive](https://www.kaggle.com/rtatman/speech-accent-archive)
- Fast speech: armenian6.wav
- Slow speech: hungarian8.wav
- Thick accent: bambara4.wav
- Normal speech: serbian9.wav
An excerpt of Trump speaking on COVID-19 was used a real life example
An exposition of the book of Philippians was used as a lengthy example (approx. 9 minutes)

## Engines
### Featured Engines
- CMUSphinx
- Google Speech Recognition

### Disqualified Engines
- IBM Watson
- Houndify
- WIT.ai

These were some of the top engines suggested in various sources about which speech recognition engines to use. Some commonly known engines that focus more on natural language processing (NLP) have been disqualified because the length of speech they are willing to process is too short to be of any practical use for the purposes of gathering data (i.e. Wit.AI, Houndify).
IBM Watson's documentation was far too confusing to follow, and there was little updated documentation on how to use it.

## Getting Started
The system is set up to make it easier to add new speech engines if needed with minimal revisions directly to the code.

### Running the project
Upon cloning the project:
```
pip install -r requirements.txt
```
Don't forget to create a virtual environment

To run the project:
```
python3 speech2.py
```
Testing
```
pytest tests
```

### Adding sound samples
Samples are stored in the `sound_samples/samples` folder. The name of each folder in this directory indicates the name of the text file the engine's hypothesis is to be compared with.
To add a new sound sample:
1) In `texts` add the text file with the actual speech in it
2) Under `sound_samples/samples` add a folder with a name matching the text file you added to `texts`
3) Under the folder add the sound file that corresponds to the text (*ensure the file is a WAV file*)

### Google Cloud Storage
**A Google Cloud Storage is required to run this project.** Create a bucket on Google Cloud Storage. Make sure your bucket in GCS reflects the same folder structure as `sound_samples`.**Only the sound files need to be uploaded to Google Cloud.** The API's hypothesis is tested against the text in the `texts` folder in the local repo.

The Google Cloud Speech Recognition API requires that sound files longer than a minute must be uploaded to Google Cloud Storage (GCS) to transcribe. For convenience, the Google Cloud Speech Recognition API in this repo is set up to acquire all its files from GCS, hence all sound files need to be in GCS for Google Cloud Speech Recognition to run.

## Assumptions
This project assumes that conversion from video to WAV or mp3 to WAV takes the same amount of time for all engines. Though whether the engine takes in MP3 files or other audio and video formats will be noted at the end of this report. As of the time of this README, it's assumed that no system is set in place to change the language bank of the speech recognition engine API, and therefore is required to be robust.

## Procedure
This project will be broken up into a series of smaller experiments testing for accuracy and latency above.

Trial procedure will consist of:
1) Feeding the sound file into the sound recognition engine
2) Recording the engine's guess and calculating the [WER](https://blog.voicebase.com/how-to-compare-speech-engine-accuracy) (using [this method](https://www.quora.com/How-do-I-measure-the-accuracy-of-speech-recognition))

The results will be saved in a spreadsheet in the root directory of this project.

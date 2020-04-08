# Imports the Google Cloud client library
from dotenv import load_dotenv
import os
import re
from google.cloud import storage
from sounds import WavInfo

load_dotenv()

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "test_speech_rec_bucket"

speech_bucket = storage_client.get_bucket(bucket_name)
all_files = [blob for blob in list(speech_bucket.list_blobs()) if re.match(r'.*\/.*\.wav', blob.name)]
trial_sounds = []
for blob in all_files:
    blob_name_parts = blob.name.split('/')
    trial_sounds.append(WavInfo(blob_name_parts[1], blob_name_parts[0], uri=f'gs://{blob.bucket.name}/{blob.name}'))
# ## 1 . Set up the audio recorder(ffmpeg and port audio)

# import logging
# import speech_recognition as sr
# from pydub import AudioSegment
# from io import BytesIO

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def record_audio(file_path, timeout=20, phrase_time_limit=None):
#     """
#     Simplified function to record audio from the microphone and save it as an MP3 file.

#     Args:
#     file_path (str): Path to save the recorded audio file.
#     timeout (int): Maximum time to wait for a phrase to start (in seconds).
#     phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
#     """

#     """What recogniser Does:
# This line creates an instance of the Recognizer class, which is used to:

# Capture audio

# Process spoken language

# Convert speech into text using APIs like Google Speech, Sphinx, Whisper, etc.
# """
#     recognizer = sr.Recognizer()
    
#     try:
#         with sr.Microphone() as source:
#             logging.info("Adjusting for ambient noise...")
#             recognizer.adjust_for_ambient_noise(source, duration=1)
#             logging.info("Start speaking now...")
            
#             # Record the audio
#             audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
#             logging.info("Recording complete.")
            
#             # Convert the recorded audio to an MP3 file
#             wav_data = audio_data.get_wav_data()
#             audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
#             audio_segment.export(file_path, format="mp3", bitrate="128k")
            
#             logging.info(f"Audio saved to {file_path}")

#     except Exception as e:
#         logging.error(f"An error occurred: {e}")


# record_audio(file_path="patient_voice_test.mp3")

# ## 2 . set up speech to tect -stt model for transcription

## 1 . Set up the audio recorder(ffmpeg and port audio)

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

from pydub.utils import which  # NEW
AudioSegment.converter = which("ffmpeg") or r"C:\Users\ritik\Downloads\ffmpeg-2025-07-17-git-bc8d06d541-essentials_build\ffmpeg-2025-07-17-git-bc8d06d541-essentials_build\bin\ffmpeg.exe"  # NEW

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """

    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


audio_filepath = "patient_voice_test.mp3"
#record_audio(file_path=audio_filepath)

## SETup speech to text model fpr transcription

import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

## Setting up the api key
api_key = os.getenv("GROQ_API_KEY")


def transcribe_with_groq(stt_model, audio_filepath, api_key):
    client=Groq(api_key=api_key)
    
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text
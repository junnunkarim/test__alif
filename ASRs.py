import os
import asr_decode
import engine

from transformers import pipeline

"""
You need to implement these functions by yourself.
These functions are used to get the speech recognition results of the corresponding API for the input audio.
The parameter "srcdir" is the directory of the audio file and "file" is the name of the file.
"trans" is the recognition result.
"""


def get_trans_tencent(srcdir, file):
    trans = ""
    return trans


def get_trans_iflytek(srcdir, file):
    trans = ""
    return trans


def get_trans_amazon(srcdir, file):
    trans = ""
    return trans


def get_trans_google(srcdir, file):
    trans = ""
    return trans


def get_trans_azure(srcdir, file):
    trans = ""
    return trans


def get_trans_whisper(srcdir, file):
    # path to the audio file
    audio_path = os.path.join(srcdir, file)

    # load the Whisper model and pipeline
    asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-base")

    # perform transcription
    result = asr_pipeline(audio_path)
    trans = result.get("text", "")  # get the transcribed text
    return trans


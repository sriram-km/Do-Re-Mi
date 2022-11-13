# import required libraries
import logging

import sounddevice as sd
from scipy.io.wavfile import write
import Util

freq = 44100
duration = 10
tempFolder = "temp/"
wavFormat = ".wav"

def recordAudio(fileName):
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    print("Listening....")
    sd.wait()
    print("Thinking....")
    write(fileName, freq, recording)

def getAudioFile():
    milliseconds = str(Util.getCurrentMilliseconds())
    fileName = tempFolder+Util.get_random_string(5)+milliseconds+wavFormat
    recordAudio(fileName)

    return fileName



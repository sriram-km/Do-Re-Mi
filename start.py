import logging
import os

import SongAction
import SongFinder
import Util
import snowboydecoder
import signal
import speech_recognition as sr
import RecordAudio
import json

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def audioRecorderCallback(fname):
    r = sr.Recognizer()
    with sr.AudioFile(fname) as source:
        audio = r.record(source)
    Util.removeFile(fname)
    try:
        command = r.recognize_google(audio)
        if command == "stop":
            global interrupted
            interrupted = True
            print("Thanks!!!")
        elif command == "start":
            print("Play the song for action")
            filename = RecordAudio.getAudioFile()
            songData = json.loads(SongFinder.findTheSong(filename))
            if (SongAction.isSongValid(songData)):
                SongAction.executeTheSong(songData)
            else:
                print("Sorry, No song found")
            Util.removeFile(filename)
        elif command == "new command":
            print("Add your custom song commands")
            filename = RecordAudio.getAudioFile()
            songData = json.loads(SongFinder.findTheSong(filename))
            Util.removeFile(filename)
            if (SongAction.isSongValid(songData)):
                command = input("Enter the command: ")
                comment = input("Enter the comment to print after execution: ")
                SongAction.addSongCommand(songData,command,comment)
            else:
                print("Sorry, No song found")
        else:
            print("Unknown command. Could you please repeat the command")
    except sr.UnknownValueError:
        print("Doremi could not understand")
    except sr.RequestError as e:
        print("Could not reach servers. Please check your internet; {0}".format(e))


model = 'resources/models/hotword.pmdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
banner= """"
  ____              ____            __  __ _ 
 |  _ \  ___       |  _ \ ___      |  \/  (_)
 | | | |/ _ \ _____| |_) / _ \_____| |\/| | |
 | |_| | (_) |_____|  _ <  __/_____| |  | | |
 |____/ \___/      |_| \_\___|     |_|  |_|_|
        
        A next level music assistant  

-----------------------------------------------------------------------

 Say Doremi to wake up Do-Re-Mi
    [+] Say "Start" to give your music command
    [+] Say "New command" to add your custom command for your favourite music
    [+] Say "Stop" to stop Do-Re-Mi
"""
print(banner)


# main loop
detector.start(detected_callback=snowboydecoder.play_audio_file,
               audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.03,
               recording_timeout=7)

detector.terminate()

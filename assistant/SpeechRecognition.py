import json
import pyaudio
from vosk import Model, KaldiRecognizer
from assistant.CommandHandler import *
import time
from assistant.Window import showPopupInBackground

jarvisActive = True

def listen():
    global jarvisActive

    activated = False
    model = Model(lang="en-us")
    recognizer = KaldiRecognizer(model, 48000)
    audio = pyaudio.PyAudio()
    mic_stream = audio.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=48000,
                            input=True,
                            frames_per_buffer=2048)
    mic_stream.start_stream()
    start_time = time.time()

    try:
        while jarvisActive:
            data = mic_stream.read(2048, exception_on_overflow=False)

            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                command = json.loads(result).get('text', '')
                print(command)
                # if activated:
                    # showPopupInBackground(command)

                respond = processCommand(command.lower(), activated)

                if respond == True and not activated:
                    start_time = time.time()
                    activated = True
                    continue

                if respond == False and activated:
                    activated = False

            elapsed_time = time.time() - start_time
            if elapsed_time >= 25 and activated:
                speak('If you need something just call me.')
                activated = False

    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        mic_stream.stop_stream()
        mic_stream.close()
        audio.terminate()

def stopListen():
    global jarvisActive
    jarvisActive = False

def continueListen():
    global jarvisActive
    jarvisActive = True
# from TTS.api import TTS
# import threading
#
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
#
# def speak_word(text):
#     threading.Thread(target=lambda: tts.tts(text=text, file_path="output.wav")).start()
#     os.system("start output.wav")


import pyttsx3

converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7)




def speak_word(text):
    try:
        converter.say(text)
        converter.runAndWait()
        converter.say(text)
        converter.runAndWait()
        converter.say(text)
        converter.runAndWait()
        converter.say(text)
        converter.runAndWait()
        print("ok","eeeeeee")
    except Exception as a:
        print(a,"eeee")



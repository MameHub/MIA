"""
Modificación del ejercicio de ejemplo para convnertir audio a texto, en este caso se utilizará un archivo de audio.
"""

import speech_recognition as sr
recognizer = sr.Recognizer
# Para utilizar un archivo de audio como origen de audio para transcribir utilizaremos la función "AudioFile()".
audio_file = sr.AudioFile('audioWAV.wav')
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio, language='ES')
print(f"El texto del audio utilizado es el siguiente:\n{text}")
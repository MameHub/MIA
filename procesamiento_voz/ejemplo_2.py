"""

"""

import speech_recognition as sr
rec = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = rec.listen(source)
to_text = rec.recognize_google(audio, language='ES')
print(to_text)
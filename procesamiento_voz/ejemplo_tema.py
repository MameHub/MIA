# Importamos la libreria "speech_recognition" y le asignamos el alias "sr", este nos facilitará las funciones necesarias.
import speech_recognition as sr
# Instanciamos el reconocimiento de voz.
recognizer = sr.Recognizer()
# Almacenamos el audio recogido por el microfono en la variable "mic".
mic = sr.Microphone()
# Definimos la variable "mic" como "source" y almacenamos en la variable "audio" lo que se obtenga con la función "listen" de la instancia de "recognizer" de la fuente "mic".
with mic as source:
    audio = recognizer.listen(source)
# Almacenamos en la variable "text" el audio obtenido en texto, en idioma español.
text = recognizer.recognize_google(audio, language = 'EN')
# Imprimimos por pantalla el audio pasado a texto.
print(f'Has dicho: {text}')
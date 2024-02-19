import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",150)
text = "Hola mundo. Este audio quedará guardado en un archivo"
output_file = "audio.mp3"
engine.save_to_file (text, output_file )
engine.runAndWait()
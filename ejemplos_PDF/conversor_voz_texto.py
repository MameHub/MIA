import pyttsx3
def convertir_texto_voz (texto):
    engine = pyttsx3.init() # Inicializa el motor de voz
    engine.say(texto) # Pasa el texto que quieres que hable
    engine.runAndWait () # Ejecuta la voz
convertir_texto_voz("Hola, soy tu asistente personal.") 
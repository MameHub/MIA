from contexto.limpieza import limpieza_texto, lista_stopwords
from contexto.vectorizacion import *

# Corpus de prueba
textos_prueba = [
    'Este es el primer texto de prueba para la vectorización y sus elementos.',
    'Una segunda oración permite evaluar si hay elementos en común para vectorizar.',
    'Tercera frase que consiste en un texto complementario con palabras comúnmente utilizadas.',
    'En esta oración y la siguiente se introducen elementos para completar un grupo de por lo menos 5.',
    'Finalmente, esta frase cierra un grupo de 5 oraciones para probar la vectorización.',
    'Una última frase para ampliar un poco el grupo.']

# Limpieza básica a los textos para quitar ruido
textos_limpios = [limpieza_texto(i, lista_stopwords(), quitar_numeros=False) for i in textos_prueba]

# Texto que no hace parte del corpus original
texto_nuevo = 'hola, este es un texto de prueba. Se desea aplicar la vectorización en este texto.'
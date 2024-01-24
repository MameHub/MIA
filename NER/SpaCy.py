import spacy
from spacy import displacy
from collections import Counter
import es_core_news_sm

nlp = es_core_news_sm.load()
doc = nlp("Carlos enseña a los alumnos a programas con NVIDIA")
print([(X.text, X.label_) for X in doc.ents])
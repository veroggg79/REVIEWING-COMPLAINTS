# -*- coding: utf-8 -*-
"""Revisando_quejas.ipynb

# Revisemos una queja

1. Escoger **un archivo** y cargar su información como una variable.
2. Determinar la longitud de dicha queja.
3. Crear una lista de palabras.
4. Eliminar las palabras que se encuentren en la lista de **stop_words_english.txt**
5. Contar las palabras y organizar por la de mayor frecuecia
6. Crear un elemento que relacione toda esta información
"""

import os

#Elegir el archivo

archivos = os.listdir('/content/complaints')
archivo_elegido = archivos[450]

archivos[0:10]

#Leer el contenido del archivo

fio_elegido = open('/content/complaints'+'/'+archivo_elegido)
texto = fio_elegido.read()
texto

longitud = len(texto)
longitud

texto_clean = texto.lower()
bolsa_palabras = texto_clean.split(" ")

len(bolsa_palabras)

bolsa_palabras[0:10]

#1. Leer stop_word
#2. Guardar en una variable (pista: hacerlo en una lista)
#3. Filtro (bolsillo/for)

#Leer el contenido del archivo

fio_stop = open('/content/stop_words_english.txt')
stop_word_english = fio_stop.read()
stop_word_english

stop_words = stop_word_english.split("\n")

stop_words[0:10]

#Manera usando un operador
bolsa_palabras[100] in stop_words

#Manera usando un método
stop_words.count(bolsa_palabras[100])!=0

bolsa_palabras_clean = []
for palabra in bolsa_palabras:
  if palabra not in stop_words:
    bolsa_palabras_clean.append(palabra)

len(bolsa_palabras),len(bolsa_palabras_clean)

freq = {}
for palabra in bolsa_palabras_clean:
  freq[palabra] = bolsa_palabras_clean.count(palabra)

freq


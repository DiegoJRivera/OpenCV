#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 22:10:24 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ************************ Access and understand pixel ************************
import cv2

# valor 1 -> indica que queremos usar colores y canales por defecto de la imagen
# valor 0 para imagen en blanco y negro
img2 = cv2.imread("images/opencv-logo.png",1)

# contenido un array enorme de valores correspondiente a los pixeles.
img2

# numpy.ndarray
type(img2)

# 739 pixels
len(img2)

# 600 valores en la fila superior -> 600 columnas
len(img2[0])

# 3 canales. R,G,B. Si hubiese una capa de transparencia serian 4
len(img2[0][0])

# (739, 600, 3) -> filas, columnas y canales....
img2.shape

# dtype('uint8'). Lo que esto nos dice es que hay un máximo de 2^8 valores en 
# cada píxel. En otras palabras, el rango de valores varía de cero a 255. 
# Esto es clave, ya que las diferentes aplicaciones o módulos en openCV, deben 
# comprender cuál es el valor máximo de una imagen y puede variar de una imagen 
# a otra. 
img2.dtype

# Se debe tener en cuenta que, en este punto, ahora se puede acceder a 
# cualquiera de los píxeles directamente mediante el uso de img, y luego usar 
# una porción para indicar a qué queremos acceder.
# 10 fila, 5 columna -> array([255, 255, 255], dtype=uint8)
# Con un max de 255 por imagen, esto seria un pixel blanco con 255, 255, 255 
# para los canales R, G y B respectivamente.
img2[10,5]

# para revisar por canal. Todas la filas, todas las columnas para el primer canal
# de la imagen
img2[:, :, 0]

# numero total de pixels -> 1330200
img2.size


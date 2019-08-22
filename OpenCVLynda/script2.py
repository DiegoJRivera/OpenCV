#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:15:28 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ************************* Data types and structures *************************
import numpy as np
import cv2

# Repasando arrays

# usando array de zeros.
# 1ero: shape or size imagen -> 150 pixels de alto, 200 
# de ancho y 1 canal.
# 2do: tipo de imagen -> 'u' por unsigned, int8 por ser potencia de 8. El rango 
# de valores permitidos en la matriz será de 0 a 255
black = np.zeros([150,200,1],'uint8')
cv2.imshow("Black",black)

# primer pixel -> 0,0 y ":" para indicar todos los valores en el pixel
print(black[0,0,:])

# lo mismo para 1's. Diferencia demasiado sutil para ojo humano, al menos el mio,
# entre matriz de 0's y 1's
ones = np.ones([150,200,3],'uint8')
cv2.imshow("Ones",ones)
print(ones[0,0,:])

# creando imagen de blanco.  Esta vez una una imagen de length de 16 bit
white = np.ones([150,200,3],'uint16')
white *= (2**16-1)
cv2.imshow("White",white)
print(ones[0,0,:])

# haciendo un deep copy (esta copiado todo su espacio en la memoria) de la 
# matriz ones.
color = ones.copy()

# asignando color. Formato BGR, creará una imagen con tenga todos los pixeles
# azules
color[:,:] = (255,0,0)
cv2.imshow("Blue",color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()

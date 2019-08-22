#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 08:14:16 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 3: Object Detection
"""
# *************************** Adaptive thresholding ***************************
'''
Si bien Simple thresholding es un algoritmo poderoso, tiene sus límites, como 
cuando hay una iluminación desigual en una imagen. Aquí es donde el Adaptive 
thresholding viene al rescate. Esta es una técnica que puede aumentar la 
versatilidad de las operaciones de umbral (thresholding) de imagen. En lugar de 
tomar un valor global simple como una comparación de umbral, el Adaptive 
thresholding buscará en su vecindario local de la imagen para determinar si se 
cumple un umbral relativo. De esta manera, es posible contrarrestar problemas, 
como la iluminación desigual.
'''
import cv2

# Leyendo imagen sudoku.png en blanco y negro (0)
img = cv2.imread('images/sudoku.png',0)
# Display de la imagen original
cv2.imshow('Original',img)

# thresholding básico para comparar iluminación de las imágenes.
# Pasando un threshold de 70 como primera estimación y el valor  máximo 
# permitido en ese formato de imagen (255)
ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
# Display de la segmentación binaria básica
cv2.imshow('Basic Binary', thresh_basic)

'''
Aquí se puede apreciar un thresholding básico, dada nuestra primera estimación 
del valor de thresholding en comparación con la imagen original. Ya se pueden 
ver algunos problemas. En la esquina superior derecha, se aprecian algunas de 
las imágenes de los números, pero en la esquina inferior izquierda, ya está 
bloqueada debido a la imagen oscura.

Usando Adaptive thresholding para hacer display correcto de la imagen completa
usando de entradas la imagen original, el valor de píxel máximo de 255, 
ADAPTIVE_THRESH_GAUSSIAN, THRESH_BINARY, seguido del parámetro de vecindad que 
indica qué tan lejos o cuál será la localización del umbral de adaptación.
Este es un valor que podemos poner como 115 y luego un valor de 1, que es una 
resta media del resultado final. Considerar la diferencia de que en el umbral 
adaptativo, solo genera una única variable, que es su imagen de umbral de salida 
real. Mientras que el umbral básico, que pone tanto un valor de retorno como un 
umbral básico.
'''
thresh_adapt = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('Adaptive Threshold', thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()

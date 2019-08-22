#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 23:00:21 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 3: Object Detection
"""
# ******************************* Skin detection ******************************
import numpy as np
import cv2

'''
Al comprender los diferentes tipos de umbrales (thresholding), se puede aplicar 
el caso de uso para detectar y segmentar los tonos de piel de una imagen. Esto 
también cubrirá el uso de filtrado compuesto para mejorar el resultado si un 
solo umbral no funcionará por sí solo. 

El archivo faces.jpeg tiene una variedad de tonos de piel para tener en cuenta. 
Ningún umbral único o umbral adaptado haría el trabajo por sí solo. Por lo 
tanto, es necesario combinar múltiples juntos. 
'''
# cargado en la imagen faces.jpeg a todo color
img = cv2.imread('images/faces.jpeg',1)

# dividiendo imagen en un formato de archivo hsv (Hue Saturation Value). 
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Dividiendo los canales individualmente
h = hsv[:,:,0] # para usar todos los píxeles para el canal de tono
s = hsv[:,:,1] # para todos los valores de los canales de saturación.
v = hsv[:,:,2] # para todos los canales de valor

# Para visualizar los canales uno al lado del otro
# axis=1 para concatenar horizontalmente
hsv_split = np.concatenate((h,s,v),axis=1)

'''
Con esto se aprecia la división de la imagen hsv. En el lado izquierdo, se ven 
los valores de matiz, el medio, los valores de saturación, a la derecha, los 
valores de intensidad reales. Considerar que los valores de tono pueden parecer 
un poco extraños.
Considerar que el tono es un parámetro circular. El rojo se indica con números 
bajos, como cero, o números muy altos, como 255. Y otros colores, como el azul 
y el verde, están en el centro, representados como los valores más grises. 
Basándose en este desglose, se puede ver que hacer una combinación de filtrado 
entre el tono y el canal de saturación dará los mejores resultados.
'''
cv2.imshow('Split HSV',hsv_split)

# Haciendo un filtro rápido en el canal de saturación. Todo en el canal de 
# saturación (s) que tenga un valor de 40 o más aparecerá como blanco.
ret, min_sat = cv2.threshold(s,40,255,cv2.THRESH_BINARY)
# Display del canal de saturacion
cv2.imshow('Sat Filter',min_sat)

# haciendo un filtro en el umbral de tono. Considerar que se va a hacer lo 
# inverso al orden normal del umbral. En este caso, esto hará que los valores 
# de cero a 15 sean blancos, y todo lo demás en negro.
ret, max_hue = cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Hue Filter',max_hue)

# combinando los filtros
final = cv2.bitwise_and(min_sat,max_hue)
'''
Se puede ver que funciona, aunque no es perfecto, pero tiene una buena 
representación de toda la piel detectada en todas estas imágenes.

Si se desglosa aún más, se puede ver el filtro de matiz y saturación. 
Al colocar la imagen final en el extremo derecho, se puede ver cómo el filtro 
de matiz se multiplica esencialmente contra el filtro de saturación para obtener 
el resultado final.

Este es un buen ejemplo de cómo el uso de múltiples filtros para el umbral 
pueden dar buenos resultados. Es importante reconocer que este no es 
necesariamente el método más robusto para detectar caras. Técnicas más avanzadas 
utilizarían machine learning o usarían métodos invariables a la luz. En este 
caso, estamos utilizando umbrales de valores codificados simples que pueden no 
funcionar en todos los entornos.

'''
cv2.imshow('Final',final)
cv2.imshow('Original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:11:44 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ********************** Image types and colors channels **********************
import numpy as np
import cv2

color = cv2.imread("images/butterfly.jpg",1)
cv2.imshow("Image",color)
# 0,0 para ubicar la imagen en la esquina izquieda superior
cv2.moveWindow("Image",0,0)
print(color.shape)
height,width,channels = color.shape

# descomponiendo los canales en cada componente como una matriz individual
b,g,r = cv2.split(color)

# creando una matriz no inicializada
rgb_split = np.empty([height,width*3,3],'uint8')

# haciendo un slice de todos los height, de zero hasta el ancho de una imagen,
# para pasar al primer canal, teniendo en cuenta que debe indicarse como una 
# imagen de tres canales. Así que se repetirá el canal azul tres veces, con b, 
# b, b en el formato de lista. Esto colocará el canal azul completamente en el 
# lado izquierdo de la imagen.
rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

# Se podran ver claramente los tres canales de rgb divididos. Es importante 
# entender que el paradigma red green blue es un método aditivo de combinar 
# colores. Para obtener el blanco se debe tener un valor máximo en cada canal, 
# así que el blanco de la mariposa aparece blanco en todas las imágenes. Pero si 
# mira el canal central, puede ver, por ejemplo, que la hoja es el color más 
# resaltado.
# Esto se debe a que es el valor más grande para el verde y luego los otros 
# canales rojo y azul de la derecha y la izquierda, respectivamente, son mucho 
# más oscuros.
cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)

# Saturación de tono y espacio de valores. Para crear esto, se creará una 
# variable llamada HSV. Esto indicará que estamos haciendo una conversión del 
# formato BGR a HSV (Hue Saturation Value). 
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# Usando comando split nuevamente -> h,s,v dividido hsv.
h,s,v = cv2.split(hsv)

# Concatenando cada uno de los canales, esta vez usando un operador np más 
# eficiente. Este es el split del guión hsv es igual a la concatenación de 
# puntos np y luego se pasará a los canales.
# usar paréntesis doble ((h,s,v)), con axis=1 para decirle al número que haga 
# que estas tres imágenes aparezcan una al lado de la otra. 
hsv_split = np.concatenate((h,s,v), axis=1)

# Las imágenes se ven muy diferentes. En el lado izquierdo está el canal de 
# tono que indica el tipo de color que vemos en un formato de 360 ​​grados. 
# En el medio está el valor de saturación que indica qué tan saturado está un 
# color individual y en el extremo derecho está el canal de valores, que indica 
# solo qué tan luminoso es el canal. Puede observar, por ejemplo, que en la 
# sección de matices, todas las hojas parecen tener el mismo color, el mismo 
# tono de oscuridad. Esta es una forma en la que puede ser más eficiente operar 
# en el espacio hsv que en el espacio rgb si, por ejemplo, se quiere aislar un 
# color en particular.
cv2.imshow("Split HSV",hsv_split)

# Tener en cuenta que los diferentes perfiles de color disponibles a medida que 
# trabaja a través de un filtrado y procesamiento más sofisticados pueden 
# encontrar una tarea casi imposible de completar en un espacio de color, pero 
# es trivial en otro.

cv2.waitKey(0)
cv2.destroyAllWindows()

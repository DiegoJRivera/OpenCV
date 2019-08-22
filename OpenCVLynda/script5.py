#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 00:47:50 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ************************ Blur, dilation and erosion *************************
# Analizando algunas funciones de filtrado útiles que se usan a menudo para 
# preprocesar o ajustar una imagen antes de realizar operaciones más complejas. 
# Estas operaciones ayudan a reducir el ruido o las variaciones no deseadas de 
# una imagen o umbral. El objetivo es hacer que la imagen sea más fácil de 
# trabajar. Los tres filtros son los filtros "Gaussian Blur", Erosion y Dilation. 

# El filtro de desenfoque gaussiano suaviza una imagen promediando los valores 
# de píxeles con sus vecinos. Se llama desenfoque gaussiano porque el promedio 
# tiene un efecto de caída gaussiano. En otras palabras, los píxeles que están 
# más cerca del píxel objetivo tienen un mayor impacto con el promedio que los 
# píxeles que están lejos. Así es como funciona el alisado. A menudo se usa como 
# una forma decente de suavizar el ruido en una imagen como un precursor de otro 
# procesamiento.
import numpy as np
import cv2

image = cv2.imread("images/thresh.jpg")
cv2.imshow("Original",image)

# Definiendo Desenfoque Gaussiano, primer parámetro -> imagen de origen, seguido 
# por el elemento estructurador que definirá cuánto desenfocar la imagen en cada 
# eje. Considerar que todos estos valores tienen que ser valores impares y 
# definir en qué medida se realiza la escala del desenfoque en cada dirección. 
# Por ejemplo, usar un valor de 5,55 desenfocará la imagen un poco en el eje x 
# y mucho más en el eje y.
# Viendo el resultado de la operación de desenfoque. Al mover la imagen borrosa 
# junto a la imagen de origen, podemos ver que, de hecho, ha difuminado la imagen 
# verticalmente mucho más que horizontalmente. También puede ver que todo el 
# ruido que estaba presente en la imagen de la mano izquierda se ha disipado en 
# su mayoría. 
blur = cv2.GaussianBlur(image,(5,55),0)
cv2.imshow("Blur",blur)

# Filtro de Dilatación y Erosión. Hay dos operaciones que buscan expandir o 
# contraer los píxeles de primer plano de una imagen para ayudar a eliminar o 
# acentuar los detalles de píxeles pequeños, como las manchas. 
# Funcionan deslizando una plantilla de kernel, un cuadrado pequeño, a través 
# de una imagen. El efecto Dilatación funciona para convertir los píxeles negros,
# o píxeles de fondo, en píxeles blancos, mientras que un filtro de erosión 
# parece convertir los píxeles blancos en píxeles negros, esencialmente devorando 
# el primer plano. El pequeño elemento estructurante que se movió a través de 
# la imagen se llama kernel y define dónde y cómo marcar un píxel cambiado por 
# ese filtro.

# Definiendo kernel. Similar al Desenfoque Gaussiano, tamaño de estructuración 
# (5,5) -> teniendo que ser valores impares en ambas dimensiones, y el tipo como 
# uint8
kernel = np.ones((5,5),'uint8')

# Definiendo filtro de dilatación distribuyendo image, el kernel, y luego se 
# establece el número de iteraciones para que sean uno.
dilate = cv2.dilate(image,kernel,iterations=1)

# Definiendo el filtro erosion, image, el kernel y luego las iteraciones
erode = cv2.erode(image,kernel,iterations=1)

# Por supuesto, si desea aumentar el efecto de cualquiera de estos filtros, los 
# niveles altos de integraciones continuarán comiendo al eje la imagen incluso 
# más que el anterior, teniendo en cuenta que cada iteración siempre se cortará 
# más desde el frente o el fondo. 

cv2.imshow("Dilate",dilate)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Se puede ver el efecto de los filtros. En el tamaño de la imagen original, que 
# tiene ruido y manchas por todas partes.
# En la ventana de Dilatación, se puede ver que todos estos puntos en el 
# primer plano, como en la mitad de la imagen, se eliminan principalmente a 
# medida que se expanden los píxeles del primer plano. También se nota que las 
# manchas que estaban en el fondo, como la esquina inferior izquierda, se 
# acentuaron y se convirtieron en manchas más grandes. De manera similar, con 
# el filtro erosionado, se ve que las manchas que estaban en el fondo, como la 
# esquina inferior izquierda, se eliminaron en su mayoría, mientras que las 
# manchas que se estaban cortando en el primer plano en el centro del objeto 
# ahora se han convertido en manchas más grandes.

# Dado el comportamiento de estos dos filtros, a veces se pueden usar juntos 
# para crear un efecto compuesto para eliminar todo el ruido.

# Junto con el Desenfoque Gaussiano, estas son herramientas poderosas para 
# filtrar y procesar imágenes, haciendo posible los cálculos más complejos.

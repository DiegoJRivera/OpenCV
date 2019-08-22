#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 02:01:00 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ************************** Scale and rotate iamges **************************
import cv2

img = cv2.imread("images/players.jpg",1)

# Algunas de las acciones de procesamiento de imágenes más básicas, pero 
# importantes, incluyen escalar y rotar.

# Scale
# img_half -> variable resize. Teniendo en cuenta que cv2.resize es la función 
# de redimensionamiento principal. Pasando en un valor de (img), luego pasando 
# el tamaño absoluto, o (0,0) para no establecer un tamaño absoluto en píxeles, 
# y luego, opcionalmente, se pueden pasar los factores relativos de fx y fy (0.5 
# para ambos casos en este ejemplo), esto dará como resultado una imagen que es 
# la mitad del tamaño en ambas dimensiones del original.
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# en img_stretch se hará un resize con un valor de (600,600), lo que significa 
# que se va a escalar explícitamente la imagen de esas dimensiones.
img_stretch = cv2.resize(img, (600,600))

# en img_stretch_near, será igual al anterior, pero esta vez Se va a configurar 
# el modo de interpolación para el proceso de escala (interpolation=cv2.INTER_NEAREST)
# Esto indicará que se va a utilizar el modo de interpolación más cercano en 
# lugar del predeterminado.
img_stretch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

# Se ve que img_stretch, se alarga verticalmente. Considerar que img_stretch_near 
# se ve un poco más pixelada porque no se realizó interpolación entre los píxeles 
# durante el proceso de escalado. Simplemente usó el píxel más cercano en 
# comparación con la imagen de origen. 

cv2.imshow("Half",img_half)
cv2.imshow("Stretch",img_stretch)
cv2.imshow("Stretch Near",img_stretch_near)

# Rotation
# Definiendo matriz de rotación. La forma en que vamos a rotar una imagen es 
# mediante la aplicación de una transformación de matriz (teniendo en cuenta 
# que las letras en mayúsculas son habituales para las definiciones de matriz)
# pasando el origen en el que queremos que se produzca la rotación (0,0), 
# girará hacia la esquina superior izquierda.Luego los grados en los que 
# queremos que se produzca la rotación. (-30 grados), entonces podemos pasar un 
# valor de uno.
M = cv2.getRotationMatrix2D((0,0),-30,1)

# Usando la matriz de transformación para rotar realmente la imagen, con 
# cv2.warpAffine, pasando la imagen, la matriz y la forma de la imagen.
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Rotated",rotated)

# Considerar que se ha movido desde la esquina superior izquierda. Si 
# hubiéramos dado, por ejemplo, la ubicación xy en la función de matriz 2D de 
# rotación, las dimensiones de la imagen en sí, habría girado realmente, desde 
# la esquina inferior derecha. Si quisiéramos rotar desde el centro de la imagen, 
# simplemente tendríamos que pasar la mitad del ancho y la mitad de la altura de 
# la imagen.

# Estas operaciones de escalado y rotación son fundamentales para formatear y 
# ajustar sus entradas de imagen para satisfacer las necesidades de un problema.

cv2.waitKey(0)
cv2.destroyAllWindows()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:15:53 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 3: Object Detection
"""
# **************************** Simple thresholding ****************************

import numpy as np
import cv2

bw = cv2.imread('images/detect_blob.png',0) # 0 para cargar imagen en blanco y negro
height, width = bw.shape[0:2]
cv2.imshow('Original BW',bw)

# inicializando variable binaria. 1 indica que es una imagen binaria de un canal 
binary = np.zeros([height, width, 1],'uint8')

# cada pixel de la imagen bw será comparado con la variable de threshold
thresh = 85

# Metodo poco efectivo, pero muestra forma de revisar uno a uno los pixeles de 
# la imgen por filas y columnas. OpenCV posee funciones predeterminadas que
# realizan lo mismo.
for row in range(0,height):
    for col in range(0,width):
        if bw[row][col] > thresh:
            binary[row][col] = 255 

cv2.imshow('Slow Binary',binary)

# con funcion cv2 para Simple thresholding
ret, thresh = cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)
cv2.imshow('CV Threshold',thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:02:36 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ****************** Challenge: Create a simple drawing app *******************
# El objetivo es crear una aplicación de dibujo simple. Esta aplicación debe 
# poder pintar varios círculos en un lienzo blanco, y debe poder cambiar entre 
# dos colores diferentes.

import numpy as np
import cv2

# Variables Globales, lienzo declarado, de 500x500 pixeles. multiplicado por 255
# dará como resultado una imagen blanca.
canvas = np.ones([500,500,3],'uint8')*255
color = (0,255,0) # verde
line_width = 3
radio = 3
point = (0,0)
pressed = False # para saber cuando se presiona el mouse


# click callback
def click(event, x, y, flags, param):
    global canvas, pressed
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas,(x,y),radio,color,-1)
    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
        cv2.circle(canvas,(x,y),radio,color,-1)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",click)

# Forever draw loop -> para correr programa hasta que se presione la letra 'q'
while(True):
    cv2.imshow("canvas",canvas)
    
    # key capture every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color = (255,0,0) # azul
    elif ch & 0xFF == ord('g'):
        color = (0,255,0) # verde
    
cv2.destroyAllWindows()





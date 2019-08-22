#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:18:11 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ************************* Create custom interfaces **************************
# iniciando con codigo de script7.py
import cv2

cap = cv2.VideoCapture(0)
# Con un conocimiento práctico de cómo crear feeds de video en tiempo real, es 
# posible diseñar nuestras propias interfaces en tiempo real.
# En el video, se a dibujará un círculo en la pantalla y vamos a mover el 
# círculo según el lugar donde haya hecho click por última vez.

# Defindo variables del circulo como color (verde), grosor de la línea, radio y 
# ubicación
color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)

# funcion para capturar los clicks del mouse:
# esta función tendrá las entradas de -> event, x, y, param. 

def click(event, x, y, flags, param):
    # globalizando variables de modo de aputar y presionar globalmente para 
    # definir el codigo.
    # Esencialmente, esta es una devolución de llamada que se ejecutará cada 
    # vez que haga click con el mouse en la fuente de video y permitirá procesar 
    # cierta información. En este caso, sólo se utilizará la devolución de 
    # llamada para cambiar las coordenadas del punto. 
    global point, pressed
    # Para registrar cada evento de click en el frame del video
    if event == cv2.EVENT_LBUTTONDOWN:
        # imprimiendo las coordenadas x,y del clickeo durante la ejecucion del 
        # programa
        print("Pressed",x,y)
        # generando nueva ubicacion del circulo
        point = (x,y)

cv2.namedWindow("Frame")
# Registrando el click en el controlador de OpenCV. Con esto y con el video en 
# ejecución, cada vez que haga clic en la pantalla, el mouse hará que el círculo 
# salte a esa ubicación.
cv2.setMouseCallback("Frame",click)

while(True):
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    # inicializando el circulo, que será incoporado en el frame, con la ubicación
    # , radio, color y grosor de linea definidos previamente.
    cv2.circle(frame, point, radius, color, line_width)
    cv2.imshow("Frame",frame)
    
    ch = cv2.waitKey(1)
  
    if ch & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

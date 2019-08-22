#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 02:52:24 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ***************************** Use video inputs ******************************
import cv2
# OpenCV proporciona un fácil acceso a las fuentes de video, lo que permite que 
# las aplicaciones brinden procesamiento en tiempo real e incluso muestren la 
# salida de video procesada. En una aplicación en tiempo real, la alimentación 
# de video se toca para una imagen al comienzo de un ciclo de repetición que 
# representa el procesamiento real de la imagen que debe ocurrir. 

# Capturando o solicitando al sistema operativo el uso de la cámara. 
# cv2.VideoCapture especificando una entrada de argumento cero que indica 
# continuidad. 
cap = cv2.VideoCapture(0)

# Considerar que esto abstrae muchas de las operaciones bajo el capó que realizan 
# el sistema operativo y OpenCV para decidir qué cámara usar si hay múltiples y 
# cómo manejar el paso de frames a OpenCV. 

# bucle infinito
while(True):
    # Leyendo el flujo de captura de video. Este comando de lectura siempre 
    # leerá un nuevo fotograma de la captura de video.
    ret, frame = cap.read()
    
    # Para modificar el tamaño del video
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow("Frame",frame)
    
    # registrando una tecla de espera, porque si no registramos una salida 
    # legítima en nuestro bucle, podemos terminar atascados y tener que forzar 
    # la salida de la aplicación. En cv2.waitKey(), en lugar de pasar 0 como 
    # solía hacerlo, pasaré 1.Esto indicará que se ejecutará cada milisegundo. 
    # Si tuviera que pasar un valor de 10, esperaría 10 milisegundos antes del 
    # siguiente ciclo y así sucesivamente.
    ch = cv2.waitKey(1)
    
    # Finalmente, 'ch' es la clave real que hemos capturado. Entonces, si se 
    # quiere echar un vistazo y romper el ciclo dado que se presionó una 
    # determinada tecla, por ejemplo, podríamos ser if ch & 0xFF, considerando 
    # que el 0xFF solo es necesario si está en una máquina de 64 bits, de lo 
    # contrario, simplemente puede escribir si ch = y luego usaremos este 
    # comando para convertir el carácter 'q', por ejemplo, en la tecla que 
    # coincidirá el valor ch, si se cumple esa condición, se saldrá del bucle.
    # Tecla Q -> salir del programa
    if ch & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

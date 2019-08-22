#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:14:41 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ********************* Pixel manipulation and filtering **********************
# Profundizando en trabajo con canales de imagen y manipulación grupos de 
# píxeles. 
import cv2

color = cv2.imread("images/butterfly.jpg",1)

# A continuación, se convertirá el número de canales de tres a uno, o escala de 
# grises.
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)

# Guardando nueva imagen de nuevo en el disco con cv2.imwrite.
# Cuando ejecute el script, en lugar de mostrarlo en la interfaz de usuario, 
# simplemente escribirá este archivo en el disco.
cv2.imwrite("images/gray.jpg",gray)

# A continuación, se agregará un canal adicional a una imagen ya cargada. En 
# este caso, es habitual indicar el cuarto canal de transparencia (canal alfa). 
# Para esto se capturarán los colores individuales de la imagen en color.
# Debe tener en cuenta que en el script3 se usó CV2.split en lugar de esta 
# sintaxis. Si bien esto es un poco más detallado, usar rebanadas ya que 
# se ha dividido los canales B G y R es en realidad mucho más eficiente y rápido 
# que usar el operador CV2.split. 
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

# Luego se combinarán estos de nuevo en una sola imagen con RGBA sea = CV2.merge,
# se fusionarán los mismos canales, (b,g,r) para luego pasar a un cuarto canal 
# que actuará como la capa de transparencia. Para esto se puede reutilizar uno 
# de los canales existentes. Si, por ejemplo, desea que las partes no verdes de 
# la imagen sean transparentes, podríamos pasar por el canal G, donde un valor 
# alto o un píxel muy verde se mostrará como una capa alfa alta, es decir, no 
# transparente y cualquier cosa que tenga un valor bajo. El valor verde o cero 
# aparecería como completamente transparente. 
rgba = cv2.merge((b,g,r,g))

# luego se reescribe como rgba.png, tener en cuenta extensión PNG porque las 
# imágenes JPEG no admiten la transparencia de la imagen.
cv2.imwrite("images/rgba.png", rgba)

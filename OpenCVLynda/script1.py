#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:07:19 2019

@author: diegorivera

From: Lynda.com - OpenCV for Python Developers. by Patrick W. Crawford.
Chapter 2: Basic Image Operations
"""
# ******************** Get Started with OpenCV and Python *********************
import cv2

# lectura de la imagen
img = cv2.imread("images/opencv-logo.png")

# display de la imagen
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

cv2.imshow("Image",img)

# espera de milisegundos declarados.
cv2.waitKey(0)

# para guardar file de imagen
cv2.imwrite("images/output.jpg",img)
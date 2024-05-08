# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:33:51 2024

@author: Usuario
"""

import cv2
import numpy as np
import imutils

image = cv2.imread("ave.jpg")
ancho = image.shape[1]
alto = image.shape[0]

#Traslación
M = np.float32([[1,0,100],[0,1,150]])
imageOut = cv2.warpAffine(image,M,(ancho,alto))
#Rotación
M= cv2.getRotationMatrix2D((ancho//2,alto//2),15,1)
imageOut1 = cv2.warpAffine(image,M,(ancho,alto))
#Escalar
imageOut2 = cv2.resize(image,(600,300),interpolation=cv2.INTER_CUBIC)
# Escalando una imagen usando imutils.resize
imageOutx1 = imutils.resize(image,width=300)
imageOutx2 = imutils.resize(image,height=300)
#Recortar
imageOut3 = image[60:220,280:480]

cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen traslacion', imageOut)
cv2.imshow('Imagen rotacion', imageOut1)
cv2.imshow('Imagen escalar', imageOut2)
cv2.imshow('Imagen escalar 1 con imutils.resize',imageOutx1)
cv2.imshow('Imagen escalar 2 con imutils.resize',imageOutx2)
cv2.imshow('Imagen recortada', imageOut3)
cv2.waitKey(0)
cv2.destroyAllWindows()

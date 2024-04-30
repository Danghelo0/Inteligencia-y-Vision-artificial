# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:58:41 2024

@author: PC
"""

import cv2
import numpy as np
imagen=cv2.imread('lambo.jpg')
m,n,c=imagen.shape
##
imagenw = imagen.astype(np.float32)

Rmax = np.max(imagenw[:, :, 0])
Gmax = np.max(imagenw[:, :, 1])
Bmax = np.max(imagenw[:, :, 2])

imagen_w= np.zeros((m, n, c))
imagen_w[:, :, 0] = (255 / Rmax) * imagenw[:, :, 0]
imagen_w[:, :, 1] = (255 / Gmax) * imagenw[:, :, 1]
imagen_w[:, :, 2] = (255 / Bmax) * imagenw[:, :, 2]

imagen_w = imagen_w.astype(np.uint8)

cv2.imshow("White-Patched Image", imagen_w)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("lambo_white_patched.jpg", imagen_w)
##

imagenw=imagen.copy()
imagenw[:,:,0]=imagen[:,:,0]+170
cv2.imshow('imagen fondo amarillo',imagenw)
cv2.imwrite("imagen fondo amarillo.jpg", imagenw)
cv2.waitKey()
cv2.destroyAllWindows()

imagen=cv2.imread("imagen fondo amarillo.jpg")
imagenw = imagen.astype(np.float32)

Rmax = np.max(imagenw[:, :, 0])
Gmax = np.max(imagenw[:, :, 1])
Bmax = np.max(imagenw[:, :, 2])

imagen_w= np.zeros((m, n, c))
imagen_w[:, :, 0] = (255 / Rmax) * imagenw[:, :, 0]
imagen_w[:, :, 1] = (255 / Gmax) * imagenw[:, :, 1]
imagen_w[:, :, 2] = (255 / Bmax) * imagenw[:, :, 2]

imagen_w = imagen_w.astype(np.uint8)

cv2.imshow("White-Patch de lambo fondo amarillo", imagen_w)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("White-Patch de lambo fondo amarillo.jpg", imagen_w)
##

imagen=cv2.imread('lambo.jpg')
imagenm=imagen.copy()
imagenm[:,:,1]=imagen[:,:,1]+180
cv2.imshow('imagen fondo morado',imagenm)
cv2.waitKey()
cv2.destroyAllWindows()

imagen=cv2.imread('lambo.jpg')
imagenb=imagen.copy()
imagenb[:,:,2]=imagen[:,:,2]+190
cv2.imshow('imagen fondo azul',imagenb)
cv2.waitKey()
cv2.destroyAllWindows()


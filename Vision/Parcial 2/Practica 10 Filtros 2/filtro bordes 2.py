# -*- coding: utf-8 -*-
"""
Created on Mon May 1 00:46:21 2024

@author: PC
"""

import cv2
import numpy as np

def mostrarImagen(imagen, titulo:str=''):
    cv2.imshow(titulo, imagen)
    cv2.waitKey()
    cv2.destroyAllWindows()

imagen = cv2.imread("mosaico.jpg", 0)
m,n=imagen.shape
imagenA = np.zeros_like(imagen)
imagenB = np.zeros_like(imagen)
imagenM = np.zeros_like(imagen)


kernel1 = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernel2 = np.transpose(kernel1)


def gradiente(k, img, imgres):
    for x in range(m-2):
        for y in range(n-2):
            res=np.sum(img[x:3+x,y:3+y]*k)
            if res>50:
                imgres[x,y]=res
                
gradiente(kernel1, imagen, imagenA)
gradiente(kernel2, imagen, imagenB)
             
for x in range(m-2):
    for y in range(n-2):
        imagenM[x, y]= abs(imagenA[x,y]) + abs(imagenB[x,y])
      
mostrarImagen(imagen, titulo='original')
mostrarImagen(imagenM, titulo='resultado')
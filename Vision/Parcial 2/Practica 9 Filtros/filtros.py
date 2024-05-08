# -*- coding: utf-8 -*-
"""
Created on Mon May  6 02:13:08 2024

@author: PC
"""
import cv2
import numpy as np

imagen=cv2.imread("ave.jpg")
m,n,c=imagen.shape

imagen_gaussiana = cv2.GaussianBlur(imagen,(5,5),0)
imagen_mediana = cv2.medianBlur(imagen,5)

ruido=np.random.normal(0,1,(m,n,c))
imagen_ruido=imagen+ruido
imagen_ruido=imagen_ruido.astype(np.uint8)
kernel=np.array([[1,1,1],[1,1,1],[1,1,1]])/9
imagen_filtrada=cv2.filter2D(imagen, -1, kernel)

def pepper_and_salt(imagen,percentage):
    num=int(percentage*imagen.shape[0]*imagen.shape[1])# Número de puntos de ruido de sal y pimienta
    np.random.randint(0, imagen.shape[0])
    imagen2=imagen.copy()
    
    for i in range(num):
        X=np.random.randint(0,imagen2.shape[0]-1)# Un número entero aleatorio desde 0 hasta la longitud de la imagen, porque es un intervalo cerrado, -1
        Y=np.random.randint(0,imagen2.shape[1]-1)
        if np.random.randint(0,1) == 0: # Probabilidad en blanco y negro 55 abierto
            imagen2[X,Y] = (255,255,255)#blanco
        else:
            imagen2[X,Y] =(0,0,0)#negro
    return imagen2

imagen_sal = pepper_and_salt(imagen,0.04)# 4 por ciento de ruido de sal y pimienta

imagen_gaussiana2 = cv2.GaussianBlur(imagen_sal,(5,5),0)
imagen_mediana2 = cv2.medianBlur(imagen_sal,5)
ruido2=np.random.normal(0,1,(m,n,c))
imagen_ruido2=imagen_sal+ruido2
imagen_ruido2=imagen_ruido2.astype(np.uint8)
kernel2=np.array([[1,1,1],[1,1,1],[1,1,1]])/9
imagen_filtrada2=cv2.filter2D(imagen_sal, -1, kernel2)

cv2.imshow("imagen", imagen)
cv2.imshow("imagen ruido", imagen_ruido)
cv2.imshow("imagen gaussiana", imagen_gaussiana)
cv2.imshow("imagen mediana", imagen_mediana)
cv2.imshow("ave sal y pimienta", imagen_sal)
cv2.imshow("imagen ruido2", imagen_ruido2)
cv2.imshow("imagen gaussiana2", imagen_gaussiana2)
cv2.imshow("imagen mediana2", imagen_mediana2)

cv2.waitKey(0)
cv2.destroyAllWindows()

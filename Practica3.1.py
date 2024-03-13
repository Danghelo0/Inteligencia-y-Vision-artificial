# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:06:15 2024

@author: PC
"""

import cv2
import numpy as np

imagen=cv2.imread("lambo.jpg")
m,n,c=imagen.shape
cv2.imshow("lambo",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# imagen2=np.zeros((m,n))


# def clasificador (imagen):
#     m,n,c=imagen.shape
#     imagen2=np.zeros((m,n))
#     for x in range(m):
#         for y in range(n):
#             if 1<imagen[x,y,0]<30 and imagen[x,y,1]<20 and imagen[x,y,2]<10:
#                 imagen2[x,y]=255
#     cv2.imwrite("lambo clasificador.jpg", imagen2)
#     cv2.imshow("lambo clasificador",imagen2)

# def scalarImagen(imagen):
#     imagen2=imagen*0.5
#     cv2.imshow("lambo cromatico",imagen2)
#     cv2.imwrite("lambo cromatico.jpg", imagen2)
#     return imagen2

# def cromatica(imagen):
#     m, n, c = imagen.shape
#     imagenCrom = np.zeros((m, n, c))
#     epsilon = 1e-8
#     for x in range(m):
#         for y in range(n):
#             total_intensity = np.sum(imagen[x, y])
#             imagenCrom[x, y, 0] = imagen[x, y, 0] / (total_intensity + epsilon)
#             imagenCrom[x, y, 1] = imagen[x, y, 1] / (total_intensity + epsilon)
#             imagenCrom[x, y, 2] = imagen[x, y, 2] / (total_intensity + epsilon)
#     return imagenCrom
        
# imagen=cv2.imread("lambo.jpg")
# clasificador (scalarImagen(cromatica(imagen)))
# clasificador(imagen)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


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

cv2.imshow("White-Patched Image", imagen_w)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("lambo_white_patched.jpg", imagen_w)


imageno1=imagen*0.7
imageno1=imageno1.astype(np.uint8)
cv2.imshow("imagen -30 de brillo",imageno1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("imagen -30 de brillo.jpg", imageno1)

imageno2=imagen*0.5
imageno2=imageno2.astype(np.uint8)
cv2.imshow("imagen -50 de brillo",imageno2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("imagen -30 de brillo.jpg", imageno2)

imagenc1=imagen.copy()
imagenc1[:,:,0]=imagenc1[:,:,0]+170
cv2.imwrite("imagen fondo amarillo.jpg", imagenc1)
cv2.imshow("imagen fondo amarillo",imagenc1)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagenc2=imagen.copy()
imagenc2[:,:,1]=imagenc2[:,:,1]+180
cv2.imwrite("imagen fondo morado.jpg", imagenc2)
cv2.imshow("imagen fondo morado",imagenc2)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagenc3=imagen.copy()
imagenc3[:,:,2]=imagenc3[:,:,2]+190
cv2.imwrite("imagen fondo azul.jpg", imagenc3)
cv2.imshow("imagen fondo azul",imagenc3)
cv2.waitKey(0)
cv2.destroyAllWindows()
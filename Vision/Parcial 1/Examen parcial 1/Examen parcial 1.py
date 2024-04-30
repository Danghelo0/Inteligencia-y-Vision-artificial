# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:12:04 2024

@author: PC
"""

import cv2
import numpy as np
imagen=cv2.imread("lambo.jpg",0)
m,n=imagen.shape
cv2.imshow("imagen",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
template = cv2.imread('template.jpg',0).astype(np.int64)
w, h = template.shape
dato = 0
imagencr=np.zeros((m-w,n-h))
for x1 in range (m-w):
    for y1 in range(n-h):
        suma = 0
        for x in range(w):
            for y in range(h):
                dif = (imagen[x1+x][y1+y]-template[x][y]).astype(np.int64)
                suma = (suma + (dif*dif)).astype(np.int64)
        if dato <suma: 
            dato = suma
        imagencr[x1][y1] = suma
imagencr=imagencr/dato
cv2.imshow("imagen1",imagencr)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Leer la imagen y el template
# imagen = cv2.imread("lambo.jpg", 0)
# template = cv2.imread('template.jpg', 0)

# # Obtener dimensiones
# m, n = imagen.shape
# w, h = template.shape

# # Inicializar la imagen de resultados
# imagencr = np.zeros((m-w+1, n-h+1))

# # Recorrer la imagen
# for x1 in range(m-w+1):
#     for y1 in range(n-h+1):
#         # Extraer la sub-imagen
#         sub_image = imagen[x1:x1+w, y1:y1+h]
#         # Calcular la SSD usando operaciones vectorizadas
#         ssd = np.sum((sub_image - template)**2)
#         # Almacenar el resultado
#         imagencr[x1, y1] = ssd

# # Normalizar el resultado para visualización
# imagencr = cv2.normalize(imagencr, None, 0, 255, cv2.NORM_MINMAX)
# imagencr = np.uint8(imagencr)

# # Mostrar la imagen original y el resultado
# cv2.imshow("Imagen", imagen)
# cv2.imshow("Resultado", imagencr)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
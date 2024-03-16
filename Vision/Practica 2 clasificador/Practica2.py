# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:14:55 2024

@author: Usuario
"""

import cv2
import numpy as np

imagen=cv2.imread("lambo.jpg")
m,n,c=imagen.shape


cv2.imshow("lambo.png",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagenb=np.zeros((m,n))
cv2.imwrite("lambob.jpg", imagenb)

for x in range(m):
    for y in range(n):
        if imagen[x,y,0]>10 and imagen[x,y,1]>20 and imagen[x,y,2]>30:
            imagenb[x,y]=255
cv2.imwrite("lambob.jpg", imagenb)
cv2.imshow("lambo.png",imagenb)
cv2.waitKey(0)
cv2.destroyAllWindows()
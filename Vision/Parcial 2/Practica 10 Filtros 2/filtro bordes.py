# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:33:51 2024

@author: Usuario
"""

import cv2
import numpy as np

imagen=cv2.imread("mosaico.jpg",0)
kernel=np.array([[1,1,1],[0,0,0],[-1,-1,-1]]) #filtro kernel
m,n=imagen.shape
filtrada=np.zeros_like(imagen)

for x in range(m-2):
    for y in range(n-2):
        res=np.sum(imagen[x:x+3,y:y+3]*kernel)
        if abs(res)>150:    
            filtrada[x,y]=255
            


cv2.imshow("ori", imagen)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("filtrada", filtrada)
cv2.waitKey()
cv2.destroyAllWindows()
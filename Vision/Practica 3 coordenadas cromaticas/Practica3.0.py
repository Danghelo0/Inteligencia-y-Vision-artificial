# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:17:22 2024

@author: PC
"""

import cv2
import numpy as np

imagen=cv2.imread("lambo.jpg")
m,n,c=imagen.shape
imagenc=imagen.copy()
imagenc=imagenc.astype(np.float32)
imagen=imagen.astype(np.float32)

for x in range (m):
    for y in range(n):
        imagenc[x,y,0]=imagen[x,y,0]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
        imagenc[x,y,1]=imagen[x,y,1]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
        imagenc[x,y,2]=imagen[x,y,2]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
        
cv2.imshow("lambo cromatico",imagenc)
cv2.imwrite('lambo cromatico.jpg',imagenc)
cv2.waitKey()
cv2.destroyAllWindows()
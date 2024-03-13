# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:59:20 2024

@author: Usuario
"""

import cv2
import numpy as np
imagen=cv2.imread("lambo.jpg")
imagen=imagen.astype(np.float32)
m,n,c=imagen.shape
#cv2.imwrite("lambo1.jpg",imagen)
cv2.imshow("lambo1",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
imagenb=np.zeros((m,n))
cv2.imwrite("imagenb.jpg",imagenb)
for x in range(m):
    for y in range(n):
        if imagen[x,y,0]>10 and imagen[x,y,1]>20 and imagen[x,y,2]>30:
            imagenb[x,y]=255
cv2.imwrite("imagenb.jpg",imagenb)

imagenc=imagen*.3
imagenc=imagenc.astype(np.uint8)
cv2.imshow("lambo",imagenc)
cv2.waitKey(0)
cv2.destroyAllWindows()
imagend=imagenc.copy()
imagend[:,:,0]=imagen[:,:,0]+190
cv2.imwrite("lamboazul.jpg",imagend)
cv2.imshow("lamboazul",imagend)
cv2.waitKey(0)
cv2.destroyAllWindows()
imagene=imagen.copy()
for x in range(m):
    for y in range(n):
        for z in range(3):
            imagene[x,y,z]=imagen[x,y,z]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
imagene=imagene*255
imagene=imagene.astype(np.uint8)
cv2.imwrite("imagene.jpg",imagene)
cv2.imshow("imagene",imagene)
cv2.waitKey(0)
cv2.destroyAllWindows()
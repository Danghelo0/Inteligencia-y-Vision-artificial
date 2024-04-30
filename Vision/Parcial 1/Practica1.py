# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:21:54 2024

@author: Usuario
"""

import cv2

imagen=cv2.imread("lambo.jpg")
m,n,c=imagen.shape
cv2.imwrite("lambo.png",imagen)

cv2.imshow("lambo.png",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Mon May 2 02:03:51 2024

@author: PC
"""

import cv2
import numpy as np
from scipy import ndimage 

img = cv2.imread('ave.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#roberts
roberts_cross_v = np.array( [[1, 0 ], 
							[0,-1 ]] ) 

roberts_cross_h = np.array( [[ 0, 1 ], 
							[ -1, 0 ]] ) 

img = cv2.imread("ave.jpg",0).astype('float64') 
img/=255.0
vertical = ndimage.convolve( img, roberts_cross_v ) 
horizontal = ndimage.convolve( img, roberts_cross_h ) 

edged_img = np.sqrt( np.square(horizontal) + np.square(vertical)) 
edged_img*=255

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely


#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)


cv2.imshow("Original Image", img)
cv2.imshow("Roberts", edged_img)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)


cv2.waitKey(0)
cv2.destroyAllWindows()
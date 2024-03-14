# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:06:15 2024

@author: PC
"""

import cv2
import numpy as np

imagen=cv2.imread("lambo.jpg")
cv2.imshow("lambo",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

###############
imageno1=imagen*0.7
imageno1=imageno1.astype(np.uint8)
cv2.imshow("imagen -30 de brillo",imageno1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("imagen -30 de brillo.jpg", imageno1)

img = cv2.imread('imagen -30 de brillo.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("Imagen -30 brillo con white patch", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("Imagen -30 brillo con white patch.png", image_balanced_8bit)

#################
imageno2=imagen*0.5
imageno2=imageno2.astype(np.uint8)
cv2.imshow("imagen -50 de brillo",imageno2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("imagen -50 de brillo.jpg", imageno2)

img = cv2.imread('imagen -50 de brillo.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("Imagen -50 brillo con white patch", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("Imagen -50 brillo con white patch.png", image_balanced_8bit)

###############
imagenc1=imagen.copy()
imagenc1[:,:,0]=imagenc1[:,:,0]+170
cv2.imwrite("imagen fondo amarillo.jpg", imagenc1)
cv2.imshow("imagen fondo amarillo",imagenc1)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('imagen fondo amarillo.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("Imagen amarilla con white patch", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("Imagen amarilla con white patch.png", image_balanced_8bit)
#################

imagenc2=imagen.copy()
imagenc2[:,:,1]=imagenc2[:,:,1]+180
cv2.imwrite("imagen fondo morado.jpg", imagenc2)
cv2.imshow("imagen fondo morado",imagenc2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('imagen fondo morado.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("Imagen morada con white patch", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("Imagen morada con white patch.png", image_balanced_8bit)
################

imagenc3=imagen.copy()
imagenc3[:,:,2]=imagenc3[:,:,2]+190
cv2.imwrite("imagen fondo azul.jpg", imagenc3)
cv2.imshow("imagen fondo azul",imagenc3)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('imagen fondo azul.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("Imagen azul con white patch", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("Imagen azul con white patch.png", image_balanced_8bit)
#############
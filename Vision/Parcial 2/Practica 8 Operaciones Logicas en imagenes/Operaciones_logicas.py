# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:49:51 2024

@author: Usuario
"""

import cv2
import numpy as np

img1 = np.zeros((400,600), dtype=np.uint8)
img1[100:300,200:400] = 255
img2 = np.zeros((400,600), dtype=np.uint8)
img2 = cv2.circle(img2,(300,200),125,(255),-1)

captura = cv2.VideoCapture(0)
mask = np.zeros((480,640),dtype=np.uint8)
mask = cv2.circle(mask,(320,240),125,(255),-1)
#mask=cv2.bitwise_not(mask)
cv2.imshow('mask',mask)

AND = cv2.bitwise_and(img1,img2)
cv2.imshow('AND', AND)

NOT = cv2.bitwise_not(img1)
cv2.imshow('NOT', NOT)

OR = cv2.bitwise_or(img1,img2)
cv2.imshow('OR', OR)

XOR = cv2.bitwise_xor(img1,img2)
cv2.imshow('XOR', XOR)

cv2.waitKey(0)
cv2.destroyAllWindows()

while (captura.isOpened()):
  ret,frame = captura.read()
  
  if ret == True:
    imgMask = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('video',imgMask)
    if cv2.waitKey(1) & 0xFF == ord('s'): #Presiona s para cerrar
      break
  else: break
captura.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
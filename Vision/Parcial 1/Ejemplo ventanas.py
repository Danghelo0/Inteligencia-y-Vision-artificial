# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:12:09 2024

@author: PC
"""

import cv2
import numpy as np

def clasificador(imagen):
  m,n,c=imagen.shape
  imagent=np.zeros((m,n))
  for x in range(m):
      for y in range(n):
          if imagen[x,y,0]>10 and imagen[x,y,1]>20 and imagen[x,y,2]>30:
             imagent[x,y]=255
  imagent = imagent.astype(np.uint8)
  return imagent
  
def mostrar(imagen):
    
    cv2.imshow("in",imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
###############################################################################
############################################################################

def etiquetado(imagent):
    num_labels,labels,stats,centroides = cv2.connectedComponentsWithStats(imagent,3,cv2.CV_32S)
    return num_labels,labels,stats,centroides
    
imagen=cv2.imread ("lambo.jpg")
mostrar(imagen)
imagent = clasificador(imagen)
mostrar(imagent)

etiqueta=imagent
num_labels,labels,stats,centroides = cv2.connectedComponentsWithStats(etiqueta,3,cv2.CV_32S)
#descartamos el fondo y aislamos 
valor_max_pi = (np.max(stats[:4][1:]))/2 #asignamos el rango 
pin = np.where((stats[:,4][1:]) > valor_max_pi)
pin = pin[0]+1
mascaras = []
mascarafinal = 0 

for i in range (0, len(pin)):
    mascara = pin[i] == labels
    mascaras.append(mascara) 
    mascarasfinal = mascarafinal + mascaras[i]
#val=mascaras[1]  
#val = val.astype(np.uint8) 
cv2.rectangle(imagen, (4,5),(200,250),(255,0,0),2)
cv2.rectangle(imagen, (300,5),(500,250),(255,0,0),2)
cv2.rectangle(imagen, (570,5),(795,250),(255,0,0),2)


imagen= cv2.resize(imagen,  (799,255), interpolation=cv2.INTER_CUBIC)


cv2.imshow("in",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:12:09 2024

@author: PC
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lambo.jpg',0)
img2 = img.copy()
template = cv2.imread('template 2.jpg',0)
template1 = cv2.imread('template 1.jpg',0)
w, h = template.shape[::-1]
w1, h1 = template1.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    res1 = cv2.matchTemplate(img,template1,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)

    #If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        top_left1 = min_loc1
    else:
        top_left = max_loc
        top_left1 = max_loc1
    bottom_right = (top_left[0] + w, top_left[1] + h)
    bottom_right1 = (top_left1[0] + w1, top_left1[1] + h1)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)
    cv2.rectangle(img, top_left1, bottom_right1, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
     
cv2.rectangle(img2, top_left, bottom_right, (255, 0, 0), 2)
cv2.rectangle(img2, top_left1, bottom_right1, (0, 255, 0), 2)  
cv2.imshow("Image", img2)
cv2.imshow("Template", template)
cv2.imshow("Template1", template1)
image = img.copy()
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
Created on 26 Jan 2018

@author: Fei Zhang
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pic/23_1.jpg',0)

kernel = np.ones((5,5),np.float32)/50

#dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

#dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
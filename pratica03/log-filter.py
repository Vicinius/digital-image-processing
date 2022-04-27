import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# read readme.md for more info

img = cv2.imread('pratica03/napoli_mall_low_intensity.png',
                 cv2.IMREAD_UNCHANGED)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
epsilon = np.finfo(float).eps  # evita logaritmo de zero
# operação logarítmica
L = 256
c = (L - 1)/np.log(L)
x, y, channels = np.shape(img)
# img de saida
g_hsv = img_hsv
for j in range(0, y):
    for i in range(0, x):
        g_hsv[i, j, 2] = c*np.log(img[i, j, 2] + epsilon)
out = cv2.cvtColor(g_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('image after log filter', out)
cv2.imshow('original image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

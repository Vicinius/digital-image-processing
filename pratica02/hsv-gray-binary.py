import cv2
import numpy as np

img1 = cv2.imread('pratica02/cameraman.tif', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('pratica02/morangos.tif', cv2.IMREAD_UNCHANGED)

img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img2_Cinza = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
thresh, img_bin = cv2.threshold(img2_Cinza, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('img2 hsv', img2_hsv)
cv2.imshow('img2', img2)
cv2.imshow('img2 cinza', img2_Cinza)
cv2.imshow('img binary', img_bin)
print(int(thresh))
cv2.waitKey(0)

# exibe imagens em hsv, cinza e binary

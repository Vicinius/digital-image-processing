import cv2
import numpy as np

img1 = cv2.imread('pratica02/cameraman.tif', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('pratica02/morangos.tif', cv2.IMREAD_UNCHANGED)

print(img1.shape, img2.shape)

# python exibe em BGR => B=0 G=1 R=2
red2 = img2[:, :, 2]
blue2 = img2[:, :, 0]
green2 = img2[:, :, 1]
stacked = np.dstack((blue2, green2, red2))

cv2.imshow('stacked', stacked)
#cv2.imshow('', img1)
cv2.imshow('original image', img2)
cv2.imshow('red channel', red2)
cv2.imshow('blue channel', blue2)
cv2.imshow('green channel', green2)


cv2.waitKey(0)

# importing libraries
import cv2 as cv
from cv2 import BORDER_CONSTANT
from cv2 import BORDER_DEFAULT
import numpy as np

moon = cv.imread('pratica04/moon.png', cv.IMREAD_UNCHANGED)

# definindo a mask de média (alterar apenas n)
n = 5
maskMean = np.ones((n, n))/(n*n)
maskLaplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# convolution
imgMean = cv.filter2D(moon, -1, maskMean)

cv.imshow('no filter', moon)
cv.imshow('filter mean', imgMean)
cv.waitKey(0)

pompei = cv.imread('pratica04/pompeii.tif', cv.IMREAD_UNCHANGED)

sobel = cv.Sobel(pompei, -1, 1, 1, borderType=BORDER_DEFAULT)
cv.imshow('borders with sobel', sobel)
cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# loading an image as it is stored in the disk
img = cv.imread('pratica05/pepitas.png', cv.IMREAD_UNCHANGED)
# converting RGB image to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# thresholding value of 100
img_bin = img_gray < 100

# Se o valor do pixel é menor que o thresh, é 0, se maior, 1
ret, thresh1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)
# isso no THRESH_BINARY, se inverso, preto vira 255 (branco) e branco vira 0 (preto)
cv.imshow('img original', img)
cv.imshow('img gray', img_gray)
cv.imshow('img binary', thresh1)
cv.waitKey(0)

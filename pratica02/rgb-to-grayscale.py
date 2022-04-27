import cv2
import numpy as np

img1 = cv2.imread('pratica02/cameraman.tif', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('pratica02/morangos.tif', cv2.IMREAD_UNCHANGED)

imgCinza = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# python exibe em BGR => B=0 G=1 R=2
red2 = (img2[:, :, 2])
blue2 = (img2[:, :, 0])
green2 = (img2[:, :, 1])
stacked = np.dstack((blue2, green2, red2))
print(red2.dtype, blue2.dtype, green2.dtype)
x, y, channels = img2.shape
average = np.zeros((x, y))

# extracting the mean pixel per pixel on each of RGB channels. the mean of the channels translate into the grayscale image

for i in range(x):
    for j in range(y):
        average[i, j] = (int(red2[i, j]) +
                         int(blue2[i, j]) + int(green2[i, j]))/3

# same approach but way simpler using numpy.mean

imgCinzaMean = np.uint8(np.mean(img2, axis=2))

average = np.uint8(average)

# the 3 should look exactly the same
cv2.imshow('original grayscale img', imgCinza)
cv2.imshow('gray image using for loop', average)
cv2.imshow('gray image using np.mean', imgCinzaMean)
cv2.waitKey(0)

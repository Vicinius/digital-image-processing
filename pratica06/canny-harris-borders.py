import cv2 as cv
import numpy as np

img = cv.imread('pratica06/pompeii.tif', cv.IMREAD_UNCHANGED)

# using the canny border detector
img_edges = cv.Canny(img, 100, 200)

cv.imshow('Canny Borders', img_edges)
cv.imshow('Image Original', img)
cv.waitKey(0)

img2 = cv.imread('pratica06/OpenCV_Chessboard.png', cv.IMREAD_UNCHANGED)
img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# using the Harris corner detector
img_gray = np.float32(img_gray)
img_corners = cv.cornerHarris(img_gray, 2, 3, 0.04)

# result is dilated for better visualization
img_corners = cv.dilate(img_corners, None, iterations=10)

# threshold for an optimal value
# just corners higher than threshold are kept
# making corners look red
img2[img_corners > 0.01*img_corners.max()] = [0, 0, 255]

cv.imshow('harris corners', img2)
cv.waitKey(0)

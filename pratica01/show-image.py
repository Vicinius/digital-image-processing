import cv2

img = cv2.imread('pratica01/lena.tif', cv2.IMREAD_UNCHANGED)

cv2.imshow('deus', img)
cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt
# H entre 0 e 33 (cor de pele)
# S entre 58 e 255 (saturação S baixo = branco)
# V entre 30 e 255 (V = 0 preto)
min_YCrCb = np.array([0, 133, 77], np.uint8)
max_YCrCb = np.array([235, 173, 127], np.uint8)
# this YCrCb color space is way better for skin detection than the HSV one

# takes your webcam input
vid = cv2.VideoCapture(0)

while(True):

    ret, frame = vid.read()
    imageYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    skinRegionYCrCb = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)
    skinYCrCb = cv2.bitwise_and(frame, frame, mask=skinRegionYCrCb)

    cv2.imshow('segmentado', skinYCrCb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

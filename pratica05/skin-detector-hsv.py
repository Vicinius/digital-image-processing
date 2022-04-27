import cv2
import numpy as np
import matplotlib.pyplot as plt
# H entre 0 e 33 (cor de pele)
# S entre 58 e 255 (saturação S baixo = branco)
# V entre 30 e 255 (V = 0 preto)
min_HSV = np.array([0, 58, 30], dtype="uint8")
# for better results, use skin-detector-YCrCb colorspace
max_HSV = np.array([33, 255, 255], dtype="uint8")

# takes your webcam input
vid = cv2.VideoCapture(0)

while(True):

    ret, frame = vid.read()
    imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    roiSkin = cv2.inRange(imageHSV, min_HSV, max_HSV)
    skin = cv2.bitwise_and(frame, frame, mask=roiSkin)

    cv2.imshow('segmentado', skin)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

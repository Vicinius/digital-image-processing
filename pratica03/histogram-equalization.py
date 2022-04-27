from operator import eq
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# exibir simples histograma de uma imagem
img_hist = cv2.imread('pratica03/pompeii_low_contrast.png', 0)
plt.hist(img_hist.ravel(), 256, [0, 256])
plt.show()

# exibir histograma equalizado
img = cv2.imread('pratica03/pompeii_low_contrast.png', cv2.IMREAD_UNCHANGED)
print(img.shape)
equalized = cv2.equalizeHist(img)
plt.hist(equalized.ravel(), 256, [0, 256])
plt.show()

cv2.imshow('img normal', img)
cv2.imshow('img equalized', equalized)
cv2.waitKey(0)

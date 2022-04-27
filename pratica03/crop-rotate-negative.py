import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# when you run this one you should wait a little while after closing the cv2.imshow initial windows,
# it will open the others on windows image viewer by default

imag = cv2.imread('pratica03/prc_papa.jpg', cv2.IMREAD_UNCHANGED)
y = 85
x = 325
h = 200
w = 475
crop = imag[y:h, x:w]  # 1
cv2.imshow('Original', imag)
cv2.imshow('Image Cropped', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

im = Image.open("pratica03/prc_papa.jpg")
left = 325
top = 85
right = 475
bottom = 200
im1 = im.crop((left, top, right, bottom))
im1.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

rotacao_im = im.rotate(90)
rotacao_im.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

im = Image.open("pratica03/prc_papa.jpg")
negative = Image.new(im.mode, im.size)  # cria nova instância

width, height = im.size  # armazena as dimensões da img
for i in range(width):  # percorre a largura
    for j in range(height):  # percorre a altura
        # .getpixel trás para cada pixel o valor de r, g e b
        r, g, b = im.getpixel((i, j))
        # substitui cada pixel por 255 - R,G,B
        negative.putpixel((i, j), (255-r, 255-g, 255-b))

negative.show()
cv2.waitKey(0)

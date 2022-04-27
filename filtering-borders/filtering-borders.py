from math import floor
import cv2
import numpy as np


def filterIMG(img, mask, **kwargs):
    if mask.shape[0] != mask.shape[1]:
        print('mask is not a square matrix')
        return False
    if mask.shape[0] % 2 != 1 or mask.shape[1] % 2 != 1:
        print('mask has even dimensions')
        return False

    typeOptions = ['default', 'zero', 'replicate']
    # a) DEFAULT: a imagem de saída com dimensões menores que a imagem de entrada, ou seja, o tratamento da borda não é realizado;
    # b) ZERO: a imagem de saída do mesmo tamanho da imagem de entrada realizando-se zero-padding;
    # c) REPLICATE: a imagem de saída do mesmo tamanho da imagem de entrada realizando-se a replicação das bordas da imagem.
    typeFilter = kwargs.get('typeFilter')
    if typeFilter == None:
        typeFilter = typeOptions[0]
    if not(typeFilter in typeOptions):
        typeFilter = typeOptions[0]

    xMask = mask.shape[0]
    xLim = floor(xMask/2)
    yMask = mask.shape[1]
    yLim = floor(yMask/2)

    xImg = img.shape[0]
    yImg = img.shape[1]

    # checa se a máscara não é maior que a imagem em x ou y
    if xImg < xMask+1 or yImg < yMask+1:
        print('mask is bigger than image')
        return False

    # aplica o filtro default, onde a imagem de saída é menor por 2*xLim e 2*yLim
    if typeFilter == 'default':
        imgToFilter = img
        imgFiltered = np.zeros((xImg-2*xLim, yImg-2*yLim))
    # aplica o filtro zero padding, onde a imagem de saída é do mesmo tamanho, acrescida por zeros nas bordas
    elif typeFilter == 'zero':
        imgToFilter = np.zeros((xImg+2*xLim, yImg+2*yLim))
        imgToFilter[xLim:xImg+xLim, yLim:yImg+yLim] = img
        imgFiltered = np.zeros((xImg, yImg))
    # aplica o filtro de replicação de borda, onde a imagem de saída é do mesmo tamanho, acrescida pelos valores das bordas
    elif typeFilter == 'replicate':
        imgToFilter = np.zeros((xImg+2*xLim, yImg+2*yLim))
        imgToFilter[xLim:xImg+xLim, yLim:yImg+yLim] = img

        for row in range(0, xLim):
            imgToFilter[row, :] = imgToFilter[xLim, :]
        for row in range(imgToFilter.shape[0]-yLim, imgToFilter.shape[0]):
            imgToFilter[row, :] = imgToFilter[imgToFilter.shape[0]-yLim-1, :]

        for col in range(0, yLim):
            imgToFilter[:, col] = imgToFilter[:, yLim]
        for col in range(imgToFilter.shape[1]-xLim, imgToFilter.shape[1]):
            imgToFilter[:, col] = imgToFilter[:, imgToFilter.shape[1]-xLim-1]

        imgFiltered = np.zeros((xImg, yImg))

    xStart = xLim
    xEnd = imgToFilter.shape[0] - 1 - xLim
    yStart = yLim
    yEnd = imgToFilter.shape[1] - 1 - yLim

    xFilter = 0
    yFilter = 0
    for xIndex in range(xStart, xEnd):
        for yIndex in range(yStart, yEnd):
            subImg = imgToFilter[xIndex-xLim:1 +
                                 xIndex+xLim, yIndex-yLim:1+yIndex+yLim]
            subImg = subImg*mask
            # realiza a convolução propriamente dita entre a subregião da img e a mask
            sumImg = subImg.sum()

            imgFiltered[xFilter, yFilter] = sumImg
            yFilter += 1
        xFilter += 1
        yFilter = 0

    # retorna os elementos do np array convertidos para uint8
    return imgFiltered.astype(np.uint8)


if __name__ == "__main__":
    # definir a imagem utilizada no formato 'img.jpg'
    fname = 'filtering-borders/prc_papa.jpg'
    img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

    n = 5
    # definir a máscara a ser utilizada, de dimensões ímpares e quadrada
    mask = np.ones((n, n))/(n*n)

    # ex: laplaciano
    # mask = np.array((
    #     [0, 1, 0],
    #     [1, -4, 1],
    #     [0, 1, 0]), dtype="int")

    # aqui você deve mudar o typeFilter para o tipo de tratamento de borda desejado
    imgfiltered = filterIMG(img, mask, typeFilter='replicate')

    cv2.imshow('original image', img)
    # checa se o tratamento de borda foi aplicado ou não
    print('original size', img.shape)
    cv2.imshow('filtered image', imgfiltered)
    # checa se o tratamento de borda foi aplicado ou não
    print('filtered size', imgfiltered.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

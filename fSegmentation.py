'''------------------Carlos Eduardo Cujcuj------------------'''
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import plot


inputImg, outputImg = sys.argv[1:]

imagenInput = np.array(cv2.imread(inputImg, 0))

def imgpad(img, r):

    """
    Descripcion de la funcion imgpad:
        Args:
            img (numpy.ndarray): array de 2 dimensiones que representa una imagen en escala
                                    de grises

            r (int): numero de pixeles que la nueva imagen generada tendra como padding
    """

    newImg = np.full( (img.shape[0]+r*2, img.shape[1]+r*2), 255)
    newImg[r:-r , r:-r] =  img

    return newImg


"""Disjoint"""

'''Source code: https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d'''
def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]

'''Source code: https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d'''
def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj


"""Connected_c"""

def connected_c(img):

    """
    Descripcion de la funcion connected_c:
        Args:
            img (numpy.ndarray): array de 2 dimensiones que representa una imagen en escala
                                    de grises
    """
    #threshold == 127
    img = np.array([[255 if img[j,i] > 127 else 0 for i in range(img.shape[1])] for j in range((img.shape[0]))])
    img = imgpad(img, 1)
    labels = np.full((img.shape[0], img.shape[1]), 255)

    contador = 0
    cont2 = 0
    disArr = [0]

    for row in range(1, img.shape[0]-1):
        for col in range(1, img.shape[1]-1):

            if img[row, col] == 0:
                a,b,c = labels[row-1,col-1], labels[row-1,col], labels[row-1,col+1]
                d,e   = labels[row,col-1], labels[row, col+1]
                f,g,h = labels[row+1,col-1], labels[row+1, col], labels[row+1, col+1]

                values = [a,b,c,d,e,f,g,h]

                if all(v == 255 for v in values):
                    contador += 1
                    disArr.append(contador)
                    labels[row, col] = contador
                    union(disArr, contador,contador)
                else:
                    vals = [i for i in values if i!= 255]
                    labels[row, col] = min(vals)
                    [union(disArr, i, min(vals)) for i in vals]

    #----Second Pass -----

    for row in range(1, labels.shape[0]-1):
        for col in range(1, labels.shape[1]-1):
            if labels[row, col] != 255:
                if labels[row, col] != find(disArr, labels[row, col]):
                    labels[row, col] = find(disArr, labels[row, col])


    return labels


"""Labelview"""

def labelview(labels):

    """
    Descripcion de la funcion labelview:
        Args:
            labels (numpy.ndarray): array  de 2 dimensiones que representa las
                                    labels generadas por la funcion connected_c

    """

    #Colores en RGB
    #pallete 1
    colores = [[69, 245, 10], [224, 27, 109], [17, 237, 200], [17, 21, 237], [89, 13, 219], [227, 242, 12]]

    #pallete 2
    #colores = [[4, 218, 173], [0, 188, 174], [0, 158, 165], [0, 128, 146], [35, 99, 120], [47, 72, 88]]

    #pallete 3
    #colores = [[209, 25, 69], [181, 40, 111], [136, 63, 134], [87, 75, 134], [51, 77, 116], [47, 72, 88]]

    #pallete 4
    #colores = [[228, 242, 10], [115, 220, 88], [0, 187, 130], [0, 149, 145], [0, 110, 129], [47, 72, 88], [72, 55, 102]]


                                 #fila,       columna,    colores
    labelColors = np.full((labels.shape[0], labels.shape[1], 3), 0, dtype = int)
    auxColors = [[0,0,0]]
    LabCol = {}
    cont = 0
    lb = 1

    for row in range(0, labels.shape[0]):
        for col in range(0, labels.shape[1]):

            if labels[row, col] != 255:
                if str(labels[row, col]) in LabCol:

                    labelColors[row][col] = LabCol[ str(labels[row, col]) ]

                else:
                    if cont == len(colores)-1:
                        cont = 0
                    else:
                        cont += 1

                    LabCol[ str(labels[row, col]) ] = colores[cont]
                    labelColors[row][col] = colores[cont]

    return labelColors


#plot.imgview(labelview(connected_c(imagenInput)), filename=outputImg)
result = labelview(connected_c(imagenInput))
#convert to float32 so we can convert BRG colors to RGB
result = result.astype(np.float32)
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
cv2.imwrite('{}'.format(outputImg),   result )
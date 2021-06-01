import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/lena.jpg")

result = []
result2 = []

cont = 0
for i in range(len(img)):
        
    bandaRLinha = utils.getArrayBandaLine(img, 0 , i) 
    bandaGLinha = utils.getArrayBandaLine(img, 1 , i)
    bandaBLinha = utils.getArrayBandaLine(img, 2 , i)
    
    dataR = dct.dct(bandaRLinha)
    dataG = dct.dct(bandaGLinha)
    dataB = dct.dct(bandaBLinha)

    pixel = []
    line = []
        
    for k in range(len(dataR)):
        pixel = [dataR[k] , dataG[k], dataB[k]]
        line.append(pixel)
        
    result.append(line)

for j in range(len(img[0])):
    
    bandaRCol = utils.getArrayBandaCol(result, 0 , j)
    bandaGCol = utils.getArrayBandaCol(result, 1 , j)
    bandaBCol = utils.getArrayBandaCol(result, 2 , j)

    dataR = dct.dct(bandaRCol)
    dataG = dct.dct(bandaGCol)
    dataB = dct.dct(bandaBCol)

    pixel = []
    col = []
        
    for k in range(len(dataR)):
        pixel = [dataR[k] , dataG[k], dataB[k]]
        col.append(pixel)
        
    result2.append(col)

print(result2)
print(len(result2) * len(result2[0]))
cv.imwrite("./sources/result.jpg", np.array(result2))

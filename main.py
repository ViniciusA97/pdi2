import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/lena.jpg")

print("Iniciando DCT")
result = img[:]
resultDCT = img[:]

#img = np.float32(img)
cv.imshow("img", img)
cv.waitKey(0)   
cv.destroyAllWindows() 

for i in range(len(img)):
    bandaRLinha = utils.getArrayBandaLine(result, 0 , i) 
    
    dataR = dct.dct(bandaRLinha)

    pixel = []
    line = []
        
    for k in range(len(dataR)):
        result[i][k][0] = dataR[k]
        result[i][k][1] = dataR[k]
        result[i][k][2] = dataR[k]

for j in range(len(img[0])):
    bandaRCol = utils.getArrayBandaCol(result, 0 , j)

    dataR = dct.idct(bandaRCol)

    pixel = []
    col = []
        
    for k in range(len(dataR)):
        result[k][j][0] = dataR[k]
        result[k][j][1] = dataR[k]
        result[k][j][2] = dataR[k]


#abs = np.abs(result)
#max = max(max(max(result.tolist())))
cv.imshow("img", img)
cv.waitKey(0)   
cv.destroyAllWindows() 
resultDCT = result [:]
print("Fim dct")
#IDCT

print("Iniciando IDCT")

resultIDCT = result[:]

"""for i in range(len(resultDCT)):
    bandaRLinha = utils.getArrayBandaLine(resultDCT, 0 , i) 
    
    dataR = dct.dct(bandaRLinha)

    pixel = []
    line = []
        
    for k in range(len(dataR)):
        resultIDCT[i][k][0] = dataR[k]
        resultIDCT[i][k][1] = dataR[k]
        resultIDCT[i][k][2] = dataR[k]
"""
"""for j in range(len(resultDCT[0])):
    bandaRCol = utils.getArrayBandaCol(resultIDCT, 0 , j)

    dataR = dct.idct(bandaRCol)

    pixel = []
    col = []
        
    for k in range(len(dataR)):
        resultIDCT[k][j][0] = dataR[k]
        resultIDCT[k][j][1] = dataR[k]
        resultIDCT[k][j][2] = dataR[k]
"""

resultDCT = np.uint8(result)
#resultIDCT = np.uint8(np.around(resultIDCT))
img = np.uint8(img)


print("----")

#utils.printImg(resultIDCT)

print("Fim IDCT.... Mostrando imagens:")
#print("rewsult idct", resultIDCT)
print("img original", img)

cv.imshow("img", img)
cv.waitKey(0)   
cv.destroyAllWindows() 

cv.imshow("idct", resultDCT)
cv.waitKey(0)   
cv.destroyAllWindows()

print("Fim IDCT.... Mostrando imagens:")

print("Salvando imagens...")
cv.imwrite("./sources/resultDCT.jpg",resultDCT)
#cv.imwrite("./sources/resultIDCT.jpg",resultIDCT)
print("Imagens salvas.")
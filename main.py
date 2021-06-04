import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/mini_lena.jpg")
ams = len(img)

result = np.copy(img)

print("Iniciando DCT")
for i in range(len(result)):
    bandaRLinha = utils.getArrayBandaLine(img, 0 , i) 
    
    dataR = dct.dct(bandaRLinha)

    pixel = []
    line = []
        
    for k in range(len(dataR)):
        result[i][k][0] = dataR[k]
        result[i][k][1] = dataR[k]
        result[i][k][2] = dataR[k]

for j in range(len(result[0])):
    bandaRCol = utils.getArrayBandaCol(result, 0 , j)

    dataR = dct.dct(bandaRCol)

    pixel = []
    col = []
        
    for k in range(len(dataR)):
        result[k][j][0] = dataR[k]
        result[k][j][1] = dataR[k]
        result[k][j][2] = dataR[k]


#abs = np.abs(result)
#max = max(max(max(result.tolist())))

resultDCT = np.copy(result)
print("Fim dct")


#IDCT
print("Iniciando IDCT")

resultIDCT = np.copy(img)

for i in range(len(resultDCT)):
    bandaRLinha = utils.getArrayBandaLine(result, 0 , i) 
    
    dataR = dct.idct(bandaRLinha)

    pixel = []
    line = []
        
    for k in range(len(dataR)):
        resultIDCT[i][k][0] = dataR[k]
        resultIDCT[i][k][1] = dataR[k]
        resultIDCT[i][k][2] = dataR[k]

for j in range(len(resultDCT[0])):
    bandaRCol = utils.getArrayBandaCol(resultIDCT,0 , j)

    dataR = dct.idct(bandaRCol)

    pixel = []
    col = []
        
    for k in range(len(dataR)):
        resultIDCT[k][j][0] = dataR[k]
        resultIDCT[k][j][1] = dataR[k]
        resultIDCT[k][j][2] = dataR[k]


resultIDCT = resultIDCT
#img = np.uint8(img)


#utils.printImg(resultIDCT)

print("Fim IDCT.... Mostrando imagens:")
#print("rewsult idct", resultIDCT)
print("img original", img)
print("img idct", resultIDCT)

cv.imshow("img", img)
cv.imshow("idct", resultIDCT)
cv.imshow("dct", resultDCT)
cv.waitKey(0)   
cv.destroyAllWindows() 

print("Fim IDCT.... Mostrando imagens:")

print("Salvando imagens...")
cv.imwrite("./sources/resultDCT.jpg",resultDCT)
print("Imagens salvas.")
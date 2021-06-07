import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/img/media_lena.png")
ams = len(img)

result = np.float32(np.copy(img))

# Faz o DCT da imagem
print("Iniciando DCT")
for i in range(len(result)):
    bandaRLinha = utils.getArrayBandaLine(result, 0 , i) 
    
    dataR = dct.dct(bandaRLinha)
        
    for k in range(len(dataR)):
        result[i][k][0] = dataR[k]
        result[i][k][1] = dataR[k]
        result[i][k][2] = dataR[k]

for j in range(len(result[0])):
    bandaRCol = utils.getArrayBandaCol(result, 0 , j)

    dataR = dct.dct(bandaRCol)
        
    for k in range(len(dataR)):
        result[k][j][0] = dataR[k]
        result[k][j][1] = dataR[k]
        result[k][j][2] = dataR[k]

# Pega o mÃ³dulo da DCT
modulo = np.abs(np.copy(result))

# Matriz zerada
matrizDeZeros = np.zeros((len(img), len(img[0]), 3))

nValores = 3
# print(f'Indice maior valor: {ind}, maior valor: {modulo[ind[0]][ind[1]][ind[2]]}')

for i in range(nValores):
    ind = np.unravel_index(np.argmax(modulo, axis=None), modulo.shape)
    matrizDeZeros[ind[0]][ind[1]][ind[2]] = result[ind[0]][ind[1]][ind[2]]
    matrizDeZeros[ind[0]][ind[1]][ind[2]+1] = result[ind[0]][ind[1]][ind[2]+1]
    matrizDeZeros[ind[0]][ind[1]][ind[2]+2] = result[ind[0]][ind[1]][ind[2]+2]
    print(f'Indice: {ind}, valor: {result[ind[0]][ind[1]][ind[2]]}')
    modulo[ind[0]][ind[1]][ind[2]] = -50
    modulo[ind[0]][ind[1]][ind[2]+1] = -50
    modulo[ind[0]][ind[1]][ind[2]+2] = -50
    



# print(matrizDeZeros)

# IDCT da imagem
print("Iniciando IDCT")


resultIDCT = np.copy(matrizDeZeros)

for i in range(len(resultIDCT)):
    bandaRLinha = utils.getArrayBandaLine(matrizDeZeros, 0 , i) 
    
    dataR = dct.idct(bandaRLinha)
        
    for k in range(len(dataR)):
        resultIDCT[i][k][0] = dataR[k]
        resultIDCT[i][k][1] = dataR[k]
        resultIDCT[i][k][2] = dataR[k]

for j in range(len(resultIDCT[0])):
    bandaRCol = utils.getArrayBandaCol(resultIDCT,0 ,j)

    dataR = dct.idct(bandaRCol)
        
    for k in range(len(dataR)):
        resultIDCT[k][j][0] = dataR[k]
        resultIDCT[k][j][1] = dataR[k]
        resultIDCT[k][j][2] = dataR[k]

print("Fim da IDCT da imagem... Mostrando imagens:")

resultIDCT = np.uint8(np.copy(resultIDCT))

cv.imshow("IDCT dos maiores valores", resultIDCT)
cv.imwrite("./sources/img/output/resultIDCT_maiores.jpg",resultIDCT)
cv.waitKey(0)   
cv.destroyAllWindows()
import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/img/media_lena.jpg")
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


# Pega o módulo da DCT
modulo = np.abs(np.copy(result))
# Pega o segundo maior valor da DCT
max = np.partition(modulo.flatten(), -4)[-4]
# Indice na matriz do maior valor
ind = np.unravel_index(np.argmax(modulo, axis=None), modulo.shape)
nivelDC = modulo[ind[0]][ind[1]][ind[2]]

print(f'\nValor do nível DC: {nivelDC}\n')

moduloSemDC = modulo/max # Divide toda a DCT pelo segundo maior valor da mesma
moduloComDC = modulo/nivelDC # Divide toda a DCT pelo valor de DC

resultIdctImagem = np.copy(result)
resultDCT = np.uint8(np.copy(result))
print("Fim dct")

# IDCT da imagem
print("Iniciando IDCT da imagem")

for i in range(len(resultIdctImagem)):
    bandaRLinha = utils.getArrayBandaLine(result, 0 , i) 
    
    dataR = dct.idct(bandaRLinha)
        
    for k in range(len(dataR)):
        resultIdctImagem[i][k][0] = dataR[k]
        resultIdctImagem[i][k][1] = dataR[k]
        resultIdctImagem[i][k][2] = dataR[k]

for j in range(len(resultDCT[0])):
    bandaRCol = utils.getArrayBandaCol(resultIdctImagem,0 ,j)

    dataR = dct.idct(bandaRCol)
        
    for k in range(len(dataR)):
        resultIdctImagem[k][j][0] = dataR[k]
        resultIdctImagem[k][j][1] = dataR[k]
        resultIdctImagem[k][j][2] = dataR[k]

print("Fim da IDCT da imagem")



# IDCT apenas do nível DC

# Cria imagem com todos os valores zerados
matrixOnlyDC = np.zeros((len(img), len(img[0]), 3))
# Adiciona o nível DC no seu índice da DCT
matrixOnlyDC[ind[0]][ind[1]][ind[2]] = nivelDC

print("Iniciando IDCT do nível DC")

resultIdctDC = np.copy(matrixOnlyDC)
for i in range(len(matrixOnlyDC)):
    bandaRLinha = utils.getArrayBandaLine(resultIdctDC, 0 , i) 
    
    dataR = dct.idct(bandaRLinha)
        
    for k in range(len(dataR)):
        resultIdctDC[i][k][0] = dataR[k]
        resultIdctDC[i][k][1] = dataR[k]
        resultIdctDC[i][k][2] = dataR[k]

for j in range(len(matrixOnlyDC[0])):
    bandaRCol = utils.getArrayBandaCol(resultIdctDC,0 ,j)

    dataR = dct.idct(bandaRCol)
        
    for k in range(len(dataR)):
        resultIdctDC[k][j][0] = dataR[k]
        resultIdctDC[k][j][1] = dataR[k]
        resultIdctDC[k][j][2] = dataR[k]


print("Fim IDCT do nível DC.... Mostrando imagens:")
resultIdctImagem = np.uint8(np.copy(resultIdctImagem))
resultIdctDC = np.uint8(np.copy(resultIdctDC))


cv.imshow("Imagem original", img)
cv.imshow("DCT com nivel DC", moduloComDC)
cv.imshow("DCT sem nivel DC", moduloSemDC)
cv.imshow("IDCT da imagem", resultIdctImagem)
cv.imshow("IDCT apenas do nivel DC", resultIdctDC)

cv.waitKey(0)   
cv.destroyAllWindows() 

print("Fim IDCT.... Mostrando imagens:")

# Normaliza os valores entre 0 e 255
moduloSemDC = moduloSemDC * 255
moduloComDC = moduloComDC * 255
resultIdctDC = resultIdctDC * 255


# print(moduloSemDC)

print("Salvando imagens...")
cv.imwrite("./sources/img/output/resultDCT.jpg",resultDCT)
cv.imwrite("./sources/img/output/resultIDCT_imagem.jpg",resultIdctImagem)
cv.imwrite("./sources/img/output/resultIDCT_DC.jpg",resultIdctDC)
cv.imwrite("./sources/img/output/moduloSemDC.jpg",moduloSemDC)
cv.imwrite("./sources/img/output/moduloComDC.jpg",moduloComDC)
print("Imagens salvas.")
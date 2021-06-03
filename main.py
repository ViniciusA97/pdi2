import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/lena.jpg")

result = img[:]
result2 = []

img = np.float32(img)


for i in range(len(img)):
    bandaRLinha = utils.getArrayBandaLine(img, 0 , i) 
    
    dataR = dct.dct(bandaRLinha)

    pixel = []
    line = []
        
    for k in range(len(dataR)):
        result[i][k][0] = dataR[k]
        result[i][k][1] = dataR[k]
        result[i][k][2] = dataR[k]

for j in range(len(img[0])):
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

result = np.uint8(result)

cv.imshow("window_name", result)
cv.waitKey(0)   
cv.destroyAllWindows() 


cv.imwrite("./sources/result.jpg",result)
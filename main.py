import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/lena.jpg")

result = img[:]
result2 = []

img = np.float32(img)/255
#print(result)
for i in range(len(img)):
    bandaRLinha = utils.getArrayBandaLine(img, 0 , i) 
    #bandaGLinha = utils.getArrayBandaLine(img, 1 , i)
    #bandaBLinha = utils.getArrayBandaLine(img, 2 , i)
    
    dataR = dct.dct(bandaRLinha)
    #dataG = dct.dct(bandaGLinha)
    #dataB = dct.dct(bandaBLinha)

    pixel = []
    line = []
        
    for k in range(len(dataR)):
        #pixel = [dataR[k] , dataG[k], dataB[k]]
        result[i][k][0] = dataR[k]
        result[i][k][1] = dataR[k]
        result[i][k][2] = dataR[k]

for j in range(len(img[0])):
    bandaRCol = utils.getArrayBandaCol(result, 0 , j)
    #bandaGCol = utils.getArrayBandaCol(result, 1 , j)
    #bandaBCol = utils.getArrayBandaCol(result, 2 , j)

    dataR = dct.dct(bandaRCol)
    #dataG = dct.dct(bandaGCol)
    #dataB = dct.dct(bandaBCol)

    pixel = []
    col = []
        
    for k in range(len(dataR)):
        result[k][j][0] = dataR[k]
        result[k][j][1] = dataR[k]
        result[k][j][2] = dataR[k]

#print(result)

#print(result)


abs = np.abs(result)

max = max(max(max(result.tolist())))

#print(max)

#result =  np.uint8(result)
result = np.uint8(result)/255
#result = result / max

#print(result)
cv.imshow("window_name", result)
cv.waitKey(0)   
cv.destroyAllWindows() 

utils.printImg(result)

cv.imwrite("./sources/result.jpg",result)




#[ 
#   [ col , col , col  ]
#   [ col , col , col  ] 
# ]


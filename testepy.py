import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/r.jpg")

print(img)
print("---linha ---")
x = utils.getArrayBandaLine(img,0,1)
print(x)
print("---col ---")
y = utils.getArrayBandaCol(img,0,1)
print(y)

result = img [:]
i= 0
for k in range(len(x)):
        #pixel = [dataR[k] , dataG[k], dataB[k]]
    result[k][i][0] = 199
    result[k][i][1] = 199
    result[k][i][2] = 199

    
print(result)

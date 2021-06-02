import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/lena.jpg",0 )

imf = np.float32(img)/255.0  # float conversion/scale
dst = cv.dct(img)           # the dct
img = np.uint8(dst)*255.0  

cv.imshow("lala",img)
cv.imwrite("./sources/resultdctopcv.jpg", img)

import dct
import cv2 as cv
import utils
import numpy as np

img = cv.imread("./sources/lena.jpg",0 )

imf = np.float32(img)/255.0  # float conversion/scale
dst = cv.dct(imf)           # the dct

img = np.uint8(dst)*255.0

cv.imshow("lala",img)
cv.waitKey(0)   
cv.destroyAllWindows() 
cv.imwrite("./sources/resultdctopcv.jpg", img)

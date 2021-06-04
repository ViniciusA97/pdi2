import dct
import cv2 as cv
import utils
import numpy as np


linha = [33 , 124, 97]

rdct = dct.dct(linha)

ridct = np.uint8(np.around(dct.idct(rdct)))
ridct = np.uint8(np.around(dct.idct(ridct)))

print("dct:", rdct)
print("-=----")
print("idct:",ridct)


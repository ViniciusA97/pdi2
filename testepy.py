import dct
import cv2 as cv
import utils
import numpy as np


linha = [154 , 124, 97]

rdct = dct.dct(linha)

ridct = np.uint(dct.idct(rdct))

print("dct:", rdct)
print("-=----")
print("idct:",ridct)


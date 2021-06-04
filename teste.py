import dct
import cv2 as cv
import utils
import numpy as np

x = [1,2,3,4,5,56]
a = x[:]

a[0] = 99999
a[1] = [111111111111111111111111111111111]
print(a)
print(x)
from pydub import AudioSegment
from pydub.utils import get_array_type
import numpy as np

x = [1,2,3]

atual_ac = -1
index = np.where(x == atual_ac)
if( len(index) == 0):
    atual_ac = atual_ac * (-1)
    print(atual_ac)
    index = np.where(x == atual_ac)
print(index)
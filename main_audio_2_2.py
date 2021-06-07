from numpy.core.fromnumeric import sort
import pydub
import numpy as np
import dct

path = "./sources/audio/"
file = "MaisUmaSemana-mp3"

audio = pydub.AudioSegment.from_mp3(path + file+".mp3")

values = np.array(audio.get_array_of_samples())

# Funcao que transforma o array em MP3
def write(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="64k")

print("---------- INICIANDO PROCESSAMENTO DE AUDIO 2.2 ---------------")
print("Tamanho do array ", len(values))
print("---------- INICIANDO PROCESSAMENTO DE AUDIO 2.2 ---------------")


print("Iniciando dct...")
ydct = dct.dct(values)
print("Dct Finalziada")

abs_ydct = np.abs(ydct)

print("Buscando nivel dc...")
max = values.max()
min = values.min()

dc = max
if(abs(min) > max):
    dc = min
index_nivel_dc = np.where(values == dc)[0][0]
print("Indice do nivel dc:" , index_nivel_dc)

print("Ordenando..")
sorted = np.partition(abs_ydct.flatten(), -1)
seccond_max = abs(sorted[-2])
print("Fim ordenação")


print("Zerando nivel dc")
ydct[index_nivel_dc] = 0
#ydct_normalizada = ydct/seccond_max

print("NIVEL DC: ", dc)
dc_nivel = [0] * len(values)
dc_nivel[index_nivel_dc] = dc

print("iniciando idct do nivel dc")
output_dc = dct.idct(dc_nivel)
write(path+file+'_2_2_nivel_dc_mp3.mp3', 44100, np.array(output_dc))

print("Iniciando idct sem o nivel dc")
output = dct.idct(ydct)
write(path+file+'_2_2_sem_dc_mp3.mp3', 44100, np.array(output))
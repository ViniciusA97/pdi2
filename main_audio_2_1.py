from numpy.core.fromnumeric import sort
import soundfile as sf
import dct
import numpy as np

path = "./sources/audio/"
file = "flute-a4"

data = sf.read(path + file +".wav")

fs = data[1]
num_amostras = len(data[0])
values = np.array(data[0])

print("---------- INICIANDO PROCESSAMENTO DE AUDIO 2.1 ---------------")
print("Tamanho do array ", len(values))
print("Arquivo: ", file)
print("---------- INICIANDO PROCESSAMENTO DE AUDIO 2.1 ---------------")


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

print("NIVEL DC: ", dc)
dc_nivel = [0] * len(values)
dc_nivel[index_nivel_dc] = dc

print("iniciando idct do nivel dc")
output_dc = dct.idct(dc_nivel)
sf.write(path+"/outputs/"+file+"_output_2_1_nivel_dc.wav", output_dc, fs)

print("Iniciando idct sem o nivel dc")
output = dct.idct(ydct)

sf.write(path+"/outputs/"+file+"_output_2_1_sem_nivel_dc.wav", output, fs)
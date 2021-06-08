import soundfile as sf
import dct
import numpy as np

path = "./sources/audio/"
file = "flute-a4"

data = sf.read(path + file +".wav")

fs = data[1]
num_amostras = len(data[0])
values = np.array(data[0])

print("---------- INICIANDO PROCESSAMENTO DE AUDIO 2.3 ---------------")
print("Tamanho do array ", len(values))
print("Arquivo: ", file)
print("---------- INICIANDO PROCESSAMENTO DE AUDIO 2.3 ---------------")

k = 1000

print("Iniciando dct...")
ydct = dct.dct(values)
print("Dct Finalziada")

print("Aplicando corte...")
corte =  np.copy(ydct)

abs = np.abs(corte)
#sorted = np.sort(abs)

output = [0] * len(values)

print("Salvando os ACS mais importantes")
for i in range(k):
    
    ind = np.argmax(abs, axis=None)
    output[ind] = ydct[ind]
    abs[ind] = -100
    
print("Iniciando idct...")
output = dct.idct(output)

sf.write(path+"/outputs/"+file+"_2_3.wav", output, fs)
#17:44 -> inicio
#18:03 - fim
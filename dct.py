import math

def dct(img):
    numAms = len(img)
    const = (2/numAms)**(0.5)
    constpi = 2*3.14

    c = 1

    result = img[:]

    #print(img)S
    
    for k in range(numAms):

        x = img[k]

        for n in range(numAms):
            precos = (constpi * n * k)/(2*numAms) + (k*3.14)/(2*numAms)
            cos = math.cos(precos)
            
            if( k == 0 ):
                c = (1/2)**0.5
            
            result[k] += (const* x * c * cos)
            c = 1
        
    return result 
    
                

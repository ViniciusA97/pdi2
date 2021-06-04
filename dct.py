import math

def dct(img):
    numAms = len(img) 
    const = (2/numAms)**(0.5)
    constpi = 2*3.14

    c = 1

    result = []
    
    for i in range(numAms):
        result.append(0)

    #print(result)
    for k in range(numAms):
                    
        if( k == 0 ):
            c = (1/2)**0.5

        for n in range(numAms):
            precos = (constpi * n * k)/(2*numAms) + (k*3.14)/(2*numAms)
            cos = math.cos(precos)
            x = img[n]
            result[k] += (const* x * c * cos)
        c = 1
        
    return result 


def idct(img):
    numAms = len(img) 
    const = (2/numAms)**(0.5)
    constpi = 2*3.14

    c = 1

    result = []
    
    for i in range(numAms):
        result.append(0)

    #print(result)
    for k in range(numAms):
                    
        if( k == 0 ):
            c = (1/2)**0.5
        x = img[k]
        for n in range(numAms):
            precos = (constpi * n * k)/(2*numAms) + (k*3.14)/(2*numAms)
            cos = math.cos(precos)
            result[n] += (const* c* x * cos)
        #result[k] = result[k] * c
        c = 1
        
    return result 
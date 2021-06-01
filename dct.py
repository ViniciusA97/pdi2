import math

def dct(img):
    n = len(img)
    const = (2/n)**(1/2)
    constpi = 2*3.14

    c = 1

    result = []

    #print(img)
    
    for k in range(n):
        #print(k)
        x = img[k] 

        precos = (constpi * n * k)/(2*n) + (k*3.14)/(2*n)
        cos = math.cos(precos)

        if( k != 0):
            c = (1/2)**1/2 
            
        result.append(x * c * cos)
        c = 1
        
    return result 
    
                

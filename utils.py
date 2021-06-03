def getArrayBandaLine(img, i, line):
    result = []
    for x in range(len(img)):
        result.append(img[line][x][i])
    return result

def getArrayBandaCol(img, i, col):
    result = []
    for x in range(len(img[0])):
        result.append(img[x][col][i])
    return result

def printImg(img):
    for i in img:
        print(i)

def writeImg(img, path):
    f = open("demofile2.txt", "w")
    for i in img:
        f.writelines(i)
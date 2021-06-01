def getArrayBandaLine(img, i, line):
    result = []
    for x in range(len(img[0])):
        result.append(img[line][x][i])
    return result

def getArrayBandaCol(img, i, col):
    result = []
    for x in range(len(img[0])):
        result.append(img[x][col][i])
    return result

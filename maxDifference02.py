def maxFindDiff(inputList):
    diffList = []
    for i in range(len(inputList)):
        if i != (len(inputList)-1):

            oneDiff = abs(inputList[i] - inputList[i+1])

            diffList.append(oneDiff)
    maxxVal = round(max(diffList), 5)
    return maxxVal

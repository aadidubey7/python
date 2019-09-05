def bubbleSort(intList):
    boolIsCheck = True

    x = -1
    while boolIsCheck:
        boolIsCheck = False
        x += 1
        for i in range(1, len(intList) - x):
            if intList[i - 1] > intList[i]:
                intList[i], intList[i - 1] = intList[i - 1], intList[i]
                boolIsCheck = True
    return intList

intList = [21, 32, 2, 6, 31, 65, 34]
output = bubbleSort(intList)
print(output)

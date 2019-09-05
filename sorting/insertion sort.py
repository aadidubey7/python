def insertionSort(intList):

    for i in range(len(intList)):
        pos = i
        element = intList[i]
        while pos > 0 and intList[pos - 1] > element:
            intList[pos] = intList[pos - 1]
            pos = pos - 1

        intList[pos] = element
    return intList
    
intList = [21, 2, 34, 12, 34, 23, 54]            
output = insertionSort(intList)
print(output)

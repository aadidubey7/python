def selectionSort(intList):
    for i in range(len(intList)):
        minimum = i
        for j in range(i + 1, len(intList)): 
            if intList[j] < intList[minimum]:
                minimum = j
        intList[i], intList[minimum]= intList[minimum], intList[i]
    return intList

intList = [12, 54, 5, 34, 78, 66]
output = selectionSort(intList)
print(output)

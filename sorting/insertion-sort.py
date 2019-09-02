def insertionSort(myList):
    for i in range(1, len(myList)):
        secondValue = myList[i]
        j = i - 1
        while j >= 0 and secondValue < myList[j]:
            myList[j + 1] = myList[j]
            myList[j] = secondValue
            j -= 1

    return myList
            

if __name__ == '__main__':
    myList = [12, 3, 5, 34, 23, 56]
    print('Before sorting', myList)
    sortedList = insertionSort(myList)
    print('After sorting', sortedList)

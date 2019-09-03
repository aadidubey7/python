def binarySearch(myItem, myList):
    boolFound = False
    bottom = 0
    top = len(myList) - 1
    intCount = 1
    while bottom <= top and not boolFound:
        middle = (bottom + top) // 2
        if int(myItem) == int(myList[middle]):
            boolFound = True
            #print('found', myItem, 'at', middle, 'on the conunter of', intCount )
        elif int(myItem) > int(myList[middle]):
            bottom = middle + 1
        else:
            top = middle - 1
        intCount += 1
    return boolFound
    

#binarySearch(12, [1, 2, 4, 6, 8, 9, 12, 35])   

if __name__ == '__main__':
    myItem = input('What number are you looking for? ')
    boolOutput = binarySearch(myItem, [1, 2, 5, 6, 8, 9, 10, 13, 56, 67, 89])
    if boolOutput:
        print('Your item is in the list.')
    else:
        print('Item does not found')

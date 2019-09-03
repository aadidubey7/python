def binarySearch(intGivenList, intSearchItem):
    boolIsFound = False
    start = 0
    end = len(intGivenList) - 1

    while start <= end and not boolIsFound:
        middle = (start + end) // 2
        
        if intSearchItem == intGivenList[middle]:
            boolIsFound = True
            break
        elif intSearchItem < intGivenList[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return boolIsFound

if __name__ == '__main__':
    intGivenList = [12, 34, 45, 65, 68, 76, 89, 90]
    intSearchItem = 90

    output = binarySearch(intGivenList, intSearchItem)
    if True == output:
        print('Item is found.')
    else:
        print('Item is not found.')

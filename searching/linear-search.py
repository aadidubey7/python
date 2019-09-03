def linearSearch(intList, intItem):
    
    boolIsFound = False
    for item in intList:
    	if item == intItem:
    		boolIsFound = True
    		break

    if True == boolIsFound:
    	print('Item is found at index', intList.index(item))
    else:
    	print('Item is not found.')

linearSearch( [1, 2, 3, 4, 5], 4 )
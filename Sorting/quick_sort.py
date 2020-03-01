#Sort the dataset using Quick sort algorithm

items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]

def quickSort(dataset, first, last):
    if first < last:
        #calculate the split point
        pivotIdx = partition(dataset, first, last)

        #now sort the two partitions 
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)

def partition(dataValues, first, last):
    #choose the first item as the pivot value
    pivotValue = dataValues[first]
    #establish the upper and the lower indices
    lower = first + 1
    upper = last

    #start searching for the crossing point
    done = False
    while not done:
        while lower <= upper and dataValues[lower] <= pivotValue:
            lower += 1
        
        while dataValues[upper] >= pivotValue and upper >= lower:
            upper -= 1
        
        #if the two indices cross, we have found the split point
        if upper < lower:
            done = True
        else:
            temp = dataValues[lower]
            dataValues[lower] = dataValues[upper]
            dataValues[upper] = temp



    #when the split point is found, exchange the pivot value
    temp = dataValues[first]
    dataValues[first] = dataValues[upper]
    dataValues[upper] = temp

    #return the split point index
    return upper


print("Dataset before sorting ",items)
quickSort(items, 0 , len(items)-1)
print("Dataset after sorting ", items)
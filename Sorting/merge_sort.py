#Sort the dataset using Merge sort algorithm

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftArray = dataset[:mid]
        rightArray = dataset[mid:]

        #recursively break down the array
        mergeSort(leftArray)
        mergeSort(rightArray)

        #now merge the arrays
        i = 0 #index into the left array
        j = 0 #index into the right array
        k = 0 #index into the merged array

        #while both arrays have content
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                dataset[k] = leftArray[i]
                i += 1
            else:
                dataset[k] = rightArray[j]
                j += 1
            k += 1

        #if the left array still has values, add them to the merged array
        while i < len(leftArray):
            dataset[k] = leftArray[i]
            i += 1
            k += 1

        #if the right array still has values, add them to the merged array
        while j < len(rightArray):
            dataset[k] = rightArray[j]
            j += 1
            k += 1
print("Dataset before sorting ", items)
mergeSort(items)
print("Dataset after sorting ", items)

        





def insertionSort(arr):
    n = len (arr)
    for i in range(1,n):
        key_item = arr[i]
        j = i-1
        while j >= 0 and key_item < arr[j] :
            arr[j + 1] = arr[j]
            j -=1
            arr[j + 1] = key_item
            return arr
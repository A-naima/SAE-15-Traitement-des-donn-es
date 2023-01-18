import numpy as np

np.random.seed(int(input("Seed:")))
y = int(input("Nombre de génération:"))

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

for i in range(y):
    s = np.random.choice(range(1, 45), 5, replace=False)
    s = list(s)
    print("Série générée :", s)
    print("Série triée :", insertionSort(s))

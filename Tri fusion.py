import numpy as np
np.random.seed(int(input("Seed:")))
y = int(input("Nombre de génération:"))


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])


    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
for i in range(y):
        s = np.random.choice(range(1, 45), 5, replace=False)
        print("Série générée :", s)
        print("Série triée :", mergesort(s))



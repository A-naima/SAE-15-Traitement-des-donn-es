import numpy as np


def binary_search_iterative(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def binary_search_recursive(arr, x, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search_recursive(arr, x, mid + 1, end)
    else:
        return binary_search_recursive(arr, x, start, mid - 1)


np.random.seed(int(input("Seed:")))
y = int(input("Nombre de génération:"))
for i in range(y):
    s = np.random.choice(range(1, 45), 5, replace=False)
    s.sort()  # Assurez-vous que la série est triée avant d'utiliser la recherche binaire
    x = np.random.randint(1, 45)  # Générer un entier aléatoire pour rechercher
    if x not in s:
        continue
    print("Série générée :", s)
    print("Entier recherché :", x)
    print("Position de l'entier recherché (itératif):", binary_search_iterative(s, x))
    result = binary_search_recursive(s, x, 0, len(s) - 1)
    print("Position de l'entier recherché (récursif):", result)


import numpy as np
x=int(input("Seed:"))
y=int(input("Nombre de génération:"))
np.random.seed(x)
for i in range (y):
    s=np.random.choice(range(1,45),5,replace=False)
    s=list(s)
    print(s)

arr = [5, 4, 3, 2, 1]

def cocktail_sort(arr):
    n = len(arr)
    a = True
    debut = 0
    fin = n-1
    while (a == True):
        a = False
        for i in range (debut,fin):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i + 1],arr[i]
                a== True
        if (a == False):
            break
        a = False
        fin = fin-1
        for i in range(fin-1, debut-1,-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i + 1],arr[i + 1],arr[i]
                a = True
        debut = debut + 1
    return arr

print(cocktail_sort(arr))
#from numpy.random import radint
import numpy as np
x=int(input("Seed:"))
y=int(input("Nombre de génération:"))
np.random.seed(0)
for i in range (y):
   s=np.random.choice(range(1,45),5,replace=False)
   s=list(s)
    print(s)

def cocktailsort(arr):
    al = True
    n = len(arr)
    debut = 0
    fin = n-1
    while (al == True):
        al = False
        for i in range (debut,fin):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i + 1],arr[i]
                al = True
        if (al == False):
            break
        al = False
        fin = fin-1
        for i in range(fin-1, debut-1,-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i + 1],arr[i + 1],arr[i]
                al = True
        debut = debut + 1
    return arr

#if __name__=='__main__':
   # x = int(input("Entrez le nombre de tirage:"))
    #for i in range(x):
       # arr = np.random.choice(range(1,45),5,replace=False)
        #arr = list(arr)
        #print(("Le tirage est :", arr))
       # print("Le tirage triée:", cocktailsort(arr))
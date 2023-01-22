import numpy as np
import matplotlib.pyplot as plt

def histogram(numbers):
    histogram = {}
    for num in numbers:
        if num in histogram:
            histogram[num] += 1
        else:
            histogram[num] = 1
    return histogram

def cocktailsort(arr):
    al = True
    n = len(arr)
    debut = 0
    fin = n-1
    while (al == True):
        al = False
        for i in range (debut,fin):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                al = True
        if (al == False):
            break
        al = False
        fin = fin-1
        for i in range(fin-1, debut-1,-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                al = True
        debut = debut + 1
    return arr

if __name__=='__main__':
    x = int(input("Entrez le nombre de tirage:"))
    np.random.seed(int(input("Seed:")))
    tirages = []
    for i in range(x):
        arr = np.random.choice(range(1,45),5,replace=False)
        arr = list(arr)
        tirages.append(arr)
        print("Le tirage est :", arr)
        print("Le tirage triée:", cocktailsort(arr))
    histo = histogram(arr)
    print("Histogramme: ", histo)
    plt.bar(histo.keys(), histo.values())
    plt.xlabel('Numero')
    plt.ylabel('Frequence')
    plt.title('Histogramme des numeros sortis')
    plt.show()

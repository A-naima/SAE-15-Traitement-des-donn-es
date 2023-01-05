
import numpy as np
x=int(input("Seed:"))
y=int(input("Nombre de génération:"))
np.random.seed(x)
for i in range (y):
    s = np.randint(40,size=(5))
    s = list(s)
    print(s)

import numpy as np
x=int(input("Seed:"))
y=int(input("Nombre de génération:"))
np.random.seed(x)
for i in range (y):
    s=np.random.choice(range(1,45),5,replace=False)
    s=list(s)
    print(s)
import numpy
a=[]
n=int(input("Enter n value : "))
for i in range(0,n):
    e= int(input("Enter element : "))
    a.append(e)
    while(len(a)>0):
      m=min(a)
      for i in range(0,len(a)):
        a[i]-=m
        b=[]
        for i in range(len(a)):
          if(a[i]>0):
            b.append(a[i])
            a=b
            print(len(a))
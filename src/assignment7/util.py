import numpy as np

def determinant(n):
    list1=[]
    for i in range(n):
        l=list(map(float,input().split()))
        list1.append(l)
    arr=np.array(list1)
    d=np.linalg.det(arr)
    print(round(d,2))
       
n=int(input())
determinant(n)
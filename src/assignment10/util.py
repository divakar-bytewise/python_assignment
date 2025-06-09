import numpy as np

def max_min(n,m):
    list1=[]
    for i in range(n):
        l=list(map(int, input().split()))
        list1.append(l)
    arr=np.array(list1)
    print(np.max(np.min(arr, axis=1)))
    
    
    
    
n,m=map(int,input().split())
max_min(n,m)


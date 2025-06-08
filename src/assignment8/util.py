import numpy as np

def mean_var_std(n,m):
    list1=[]
    for i in range(n):
        l=list(map(int,input().split()))
        list1.append(l)
    arr=np.array(list1)
    print (np.mean(arr,axis=1))
    print (np.var(arr,axis=0))
    std=np.std(arr)
    print (0.0 if std==0 else f"{std:.11f}")
    
        
n,m=map(int,input().split())
mean_var_std(n,m)

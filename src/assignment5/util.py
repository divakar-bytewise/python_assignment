import numpy as np

def convertion(n):
    #arr=np.array(n)
    np.set_printoptions(sign=" ")
    print(np.floor(n))
    print(np.ceil(n))
    print(np.rint(n))
    
    
    
n=list(map(float, input().split()))
convertion(n)



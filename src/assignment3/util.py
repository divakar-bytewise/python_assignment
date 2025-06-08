def finding_second_largest(arr):
    num=list(set(arr))
    num.sort()
    sl=num[-2]
    return sl
    
    
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    r=finding_second_largest(arr)
    print(r)

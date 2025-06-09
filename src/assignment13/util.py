from collections import deque

def can_stack_cubes(cubes):
    dq = deque(cubes)
    last = float('inf')
    
    while dq:
        if dq[0] >= dq[-1]:
            pick = dq.popleft()
        else:
            pick = dq.pop()
        
        if pick > last:
            return "No"
        last = pick
    
    return "Yes"


for _ in range(t):
    t=int(input())
    n = int(input())
    cubes = list(map(int, input().split()))
    print(can_stack_cubes(cubes))

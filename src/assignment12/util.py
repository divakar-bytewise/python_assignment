def happiness_score(n, m, arr, a, b):
    return sum((i in a) - (i in b) for i in arr)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(happiness_score(n, m, arr, a, b))

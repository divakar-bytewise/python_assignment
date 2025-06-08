from src.assignment12.util import happiness_score

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    
    print(happiness_score(n, m, arr, a, b))

from src.assignment13.util import can_stack_cubes

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        print(can_stack_cubes(cubes))

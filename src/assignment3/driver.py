from src.assignment1.util import finding_second_largest

if __name__ == '__main__':
    n=int(input("Enter number of elements: "))
    arr=list(map(int, input("Enter elements separated by space: ").split()))
    result=finding_second_largest(arr)
    print(result)

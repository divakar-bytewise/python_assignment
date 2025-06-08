from util import finding_day

if __name__ == '__main__':
    m, d, y = map(int, input("Enter month, day, year: ").split())
    result=finding_day(m, d, y)
    print(result)

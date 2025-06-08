from util import finding_avg

if __name__ == "__main__":
    n = int(input("Enter number of students: "))
    attributes = input("Enter attributes: ").split()
    result = finding_avg(n, attributes)
    print(f"{result:.2f}")

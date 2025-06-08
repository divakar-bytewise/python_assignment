from src.assignment6.util import probability_of_a

if __name__ == '__main__':
    n = int(input("Enter number of letters: "))
    letters = input("Enter letters separated by space: ").split()
    k = int(input("Enter size of combination: "))
    
    result = probability_of_a(n, letters, k)
    print(f"{result:.4f}")

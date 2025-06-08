from itertools import combinations

def probability_of_a(n, letters, k):
    indices_with_a = [i for i, letter in enumerate(letters) if letter == 'a']
    total_combinations = list(combinations(range(n), k))
    favorable = [comb for comb in total_combinations if any(i in indices_with_a for i in comb)]
    return len(favorable) / len(total_combinations)

n = int(input())
letters = input().split()
k = int(input())

result = probability_of_a(n, letters, k)
print(f"{result:.4f}")

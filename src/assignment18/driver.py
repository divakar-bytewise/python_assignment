from util import word_occurrence_counter

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]

    word_count = word_occurrence_counter(words)
    print(len(word_count))
    print(" ".join(str(count) for count in word_count.values()))

from src.assignment4.util import finding_average

if __name__ == '__main__':
    n = int(input("Enter number of students: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter name and scores: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter name to query: ")
    result = finding_average(student_marks, query_name)
    print(f"{result:.2f}")

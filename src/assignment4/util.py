def finding_average(student_marks,query_name):
    if query_name in student_marks:
        avg=sum(student_marks[query_name])/len(student_marks[query_name])
        return avg


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    r=finding_average(student_marks,query_name)
    print(f"{r:.2f}")
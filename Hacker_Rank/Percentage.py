if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    result = 0
    for name,value in student_marks.items():
        if query_name == name:
            result = sum(value)
            result = result / 3            
            break

print("%.2f" % result)
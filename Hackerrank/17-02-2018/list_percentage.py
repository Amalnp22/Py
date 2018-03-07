n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
l=[]
for i in student_marks:
    if i==query_name:
        l=student_marks[i]
print("%.2f" % (sum(l)/3))

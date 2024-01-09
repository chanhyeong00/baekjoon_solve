lst = []
total_grade = 0.0 # 총 학점
total_major = 0.0 # 전공과목별(학점x과목평점) 합
grade = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
} # 학점
grade_lst = grade.keys()
for _ in range(20):
    l = list(map(str, input().split()))
    if l[2] in grade_lst: # p가 아니면 학점과 평점을 둘 다 더함
        total_major += (float(grade[l[2]]) * float(l[1]))
        total_grade += float(l[1])

avg = total_major / total_grade
print("{:.6f}".format(avg))
from sys import stdin

input = stdin.readline

form =  input().strip().split('-') # -가 나온 순간부터 다 뻄

answer = 0

for i in form[0].split('+'):
    answer += int(i)

for i in range(1, len(form)):
    for j in form[i].split('+'):
        answer -= int(j)

print(answer)
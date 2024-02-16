from sys import stdin

input = stdin.readline

form =  input() # -가 나오면 괄호 열고, -나 맨 끝이면 괄호 닫고를 반복한다.
s = 0
flag = False
num = ''
for idx, f in enumerate(form):
    if flag == True: # 괄호 열린 상태
        if idx == len(form) - 1:
            s -= int(num)
        elif f == '-' or f == '+':
            s -= int(num)
            num = ''
        else:
            num += f
    else: # 괄호 닫힌 상태
        if idx == len(form) - 1:
            s += int(num)
        elif f == '-' or f == '+': # 이때부턴 나오는 수 전부 뺌
            s += int(num)
            if f == '-':
                flag = True
            num = ''
        else: # 연산자 아니면 숫자 이어붙임
            num += f

print(s)
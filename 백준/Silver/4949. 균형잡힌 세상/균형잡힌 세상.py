import sys
input = sys.stdin.readline

while True:
    sentence = input().strip('\n')
    answer = 'yes'
    lst = [] # 괄호 여부 확인
    if len(sentence)==1 and sentence[0] == '.':
        break
    for s in sentence:
        if s == '(':
            lst.append(s)

        elif s == '[':
            lst.append(s)
        
        elif s == ')':
            if lst and lst[-1] == '(':
                lst.pop(-1)
            else:
                answer = 'no'
                break
        elif s == ']':
            if lst and lst[-1] == '[':
                lst.pop(-1)
            else:
                answer = 'no'
                break
    if len(lst) > 0:
        answer = 'no'
    print(answer)
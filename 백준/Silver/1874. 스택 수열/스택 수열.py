import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
num = 1

for _ in range(n):
    seq_num = int(input())
    while num <= seq_num: # 찾는 수보다 작거나 같으면 계속 스택에 넣음
        stack.append(num)
        answer.append('+')
        num += 1
    if seq_num == stack[-1]: # 같다면 pop
        stack.pop(-1)
        answer.append('-')

if stack:
    print('NO')
else:
    print('\n'.join(answer))
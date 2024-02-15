from sys import stdin

input = stdin.readline

n = int(input())
lst = [i for i in range(n, 0, -1)]
stack = [lst.pop()]
cnt = 0
answer = '+'
for _ in range(n):
    element = int(input())
    if stack and stack[-1] == element:
            stack.pop()
            cnt += 1
            answer += '-'
            continue
    while lst:
        stack.append(lst.pop())
        answer += '+'
        if stack[-1] == element:
            stack.pop()
            cnt += 1
            answer += '-'
            break
if cnt == n:
    print('\n'.join(list(answer)))
else:
     print('NO')
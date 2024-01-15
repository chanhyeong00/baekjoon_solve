from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    str = stdin.readline()
    cnt = 0 # 여닫는 괄호의 수
    for s in str:
        if s == '(':
            cnt += 1
        elif s == ')':
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print('NO')
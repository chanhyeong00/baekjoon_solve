from sys import stdin
n = int(stdin.readline()) 
stack = [] # 왼쪽이 가장 아래, 오른쪽이 가장 위
cnt = 0 # 스택 정수 개수 (3을 위한)

for _ in range(n):
    order = list(map(int, stdin.readline().split()))
    if order[0] == 1:
            stack.append(order[1])
            cnt += 1
    elif order[0] == 2:
        if cnt > 0:
            print(stack.pop(-1))
            cnt -= 1
        elif cnt == 0:
            print(-1)
    elif order[0] == 3:
        print(cnt)
    elif order[0] == 4:
        if cnt == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 5:
        if cnt > 0:
            print(stack[-1])
        else:
            print(-1)

         

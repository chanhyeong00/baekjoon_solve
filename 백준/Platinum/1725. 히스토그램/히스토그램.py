from sys import stdin

input = stdin.readline

n = int(input())
h = []
for _ in range(n):
    h.append(int(input()))
    
h.append(-1)
stack = [0] # 인덱스로 스택 비교

answer = 0

for i in range(1, n+1):
    while stack and h[stack[-1]] > h[i]: # 뽑은 애가 스택 마지막보다 작으면 계산 시작
        height = h[stack.pop()]
        if not stack: # 스택 비었다면 앞까지는 모두 크거나 같은 애들
            width = i 
        else:
            width = i - stack[-1] - 1 # 스택에서 이미 빠져있어서 1 차이남
        answer = max(answer, width * height)
    stack.append(i) # 뽑은 애가 스택 마지막보다 크면 넣어준다.

print(answer)
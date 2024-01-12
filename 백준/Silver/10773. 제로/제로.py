from sys import stdin

k = int(stdin.readline())

lst = []
answer = 0

for _ in range(k):
    num = int(stdin.readline())
    if num != 0:
        lst.append(num)
        answer += num
    else:
        answer -= lst[-1]
        lst.pop(-1)
print(answer)

# 입력을 sys.readline() 으로 받으면 시간이 확 줄어든다

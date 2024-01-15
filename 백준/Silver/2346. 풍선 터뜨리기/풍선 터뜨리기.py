from sys import stdin
from collections import deque
n = int(stdin.readline())

lst = [i for i in range(1, n+1)]
balloon = deque(enumerate(map(int, stdin.readline().split())))
# enumerate 쓰면 튜플로 묶여서 저장됨
answer = []
while balloon:
    idx, num = balloon.popleft()
    answer.append(str(idx + 1))

    if num > 0: # 왼쪽으로 회전(pop left 된 1칸 제와)
        balloon.rotate(-(num - 1))
    elif num < 0: # 오른쪽 회전(음수일 떄는 영향이 없음)
        balloon.rotate(-num)
print(' '.join(answer))

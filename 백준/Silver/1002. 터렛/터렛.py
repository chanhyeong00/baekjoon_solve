import sys
t = int(sys.stdin.readline())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = ((x1 - x2) ** 2 + (y1- y2) ** 2) ** (1 / 2)
    if distance == 0 and r1 == r2: # 동심원 + 반지름 같을 때
        print(-1)
    elif abs(r1 - r2) < distance and distance < r1 + r2:
        print(2)
    elif abs(r1 - r2) == distance or r1 + r2 == distance: 
        print(1)
    else:
        print(0)
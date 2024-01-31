from sys import stdin

n = int(stdin.readline())
stair = []
mem = [-1] * n

for _ in range(n):
    stair.append(int(stdin.readline()))

mem[0] = stair[0]
def up_stair(floor):
    if floor < 0: 
        return 0
    if mem[floor] != -1: # 이미 계산된 값 있으면
        return mem[floor]
    
    mem[floor] = max(stair[floor] + up_stair(floor-2), stair[floor] + stair[floor-1] + up_stair(floor-3))

    return mem[floor]

result = up_stair(n-1)
print(result)

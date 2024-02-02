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
    
    mem[floor] = max(stair[floor] + up_stair(floor-2),\
                     stair[floor] + stair[floor-1] + up_stair(floor-3))
    # 한 계단을 밟으면 두가지 경우만 가능함
    # 아래로 2칸 내려가거나
    # 한 칸 내려간 경우는 다음에 두칸 내려가야함
    return mem[floor]

result = up_stair(n-1)
print(result)

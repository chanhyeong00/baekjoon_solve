import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
sum_ = 0
height_dict = {i:0 for i in range(257)}

for _ in range(N):
    ground = list(map(int, input().split()))
    for g in ground:
        height_dict[g] += 1
    sum_ += sum(ground)

time = float('inf')
max_height = (sum_ + B) // (N * M)
height = 0

for h in range(max_height, -1, -1): # 0~max_height 높이로 고르기
    t, b = 0, B
    for hd_h, hd_n in height_dict.items():
        if hd_h > h:
            b += ((hd_h - h) * hd_n)
            t += (2 * hd_n * (hd_h - h))
        elif hd_h < h:
            b -= ((h - hd_h)* hd_n)
            t += hd_n * (h - hd_h)
    if b >= 0 and time > t:
        time = t
        height = h
        
    
print(time, height)

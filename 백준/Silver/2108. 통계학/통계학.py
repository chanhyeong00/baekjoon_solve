import sys
input = sys.stdin.readline

N = int(input())
lst = []
pos_cnt = [0]*4001
neg_cnt = [0]*4001
sum = 0
for _ in range(N):
    num = int(input())
    lst.append(num)
    sum += num
    if num >= 0: pos_cnt[num] += 1
    else: neg_cnt[-num] += 1

print(round(sum / N)) # 산술 평균

# 중앙값
lst.sort()
mid_idx = N // 2
print(lst[mid_idx]) 

#최빈값
max_cnt = max(pos_cnt) if max(pos_cnt) >= max(neg_cnt) else max(neg_cnt)
max_lst = []
for i in range(4001):
    if max_cnt == pos_cnt[i]: 
        max_lst.append(i)
    if max_cnt == neg_cnt[i]:
        max_lst.append(-i)

max_lst.sort()
if len(max_lst) == 1:
    print(max_lst[0])
else:
    print(max_lst[1])

print(lst[-1] - lst[0]) # 범위
from sys import stdin

input = stdin.readline

n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().split())))
times.sort(key=lambda x: [x[1],x[0]]) # 끝나는 시간에 대해서 정렬(끝나는 시간이 짧을수록 회의가 많아짐)
# 종료 시간이 같으면 시작시간에 대해 정렬
start, end, cnt = -1, -1, 0
for i in range(n): # 회의 끝나고 시작 가능한지 여부 확인하고 세기
    meeting = times[i]
    if meeting[0] >= end: # 시작 시간이 이전 회의 끝나는 시간보다 크거나 같고
        cnt += 1
        end = meeting[1]

print(cnt)


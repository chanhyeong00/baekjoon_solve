from sys import stdin

input = stdin.readline

k, n = map(int, input().split())
lst = list(int(input()) for _ in range(k))

start = 1
end = max(lst)
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += (lst[i] // mid)
    if cnt >= n: # 개수가 같거나 더 많으먄(더 많은 경우는 버리기 가능)
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)

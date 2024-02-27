from sys import stdin

input = stdin.readline

n = int(input())
A = list(map(int, input().split()))

lis = [A[0]]

for i in range(1, n): # 기준 선택
    if lis[-1] < A[i]: # 넣을 수 있으면 넣음
        lis.append(A[i])
    else: # 작거나 같다면 최적값을 구하기 위해 변경해줄 자리 찾음
        start, end = 0, len(lis) - 1

        # lis 배열 탐색
        while start <= end:
            mid = (start + end) // 2

            if lis[mid] < A[i]: # lis 값이 작다면 오른쪽 탐색
                start = mid + 1
            else: # 더 크면 왼쪽 탐색
                end = mid - 1
        lis[start] = A[i] # 다 줄인 후 최적값으로 넣어준다. 
print(len(lis))
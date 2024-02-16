from sys import stdin

input = stdin.readline

n = int(input())
distances = list(map(int, input().split()))
oil = list(map(int, input().split()))

inf = []
check_pt = [0] * n
oil_l = oil[0] * distances[0] # 처음엔 무조건 주유

for i in range(1, n-1): # 인덱스, 가격
    inf.append((i, oil[i]))

inf.sort(key= lambda x:[x[1], x[0]]) # 가격순 정렬

pt, price = n, 10**9 # 특정 지점과 지불해야할 가격

for i in inf: # 정보를 돈다(가격순 정렬된 상태)
    if i[0] <= pt: # 특정 지점보다 앞에 있으면
        check_pt[i[0]] = i[1] # 그 지점보다 앞은 이 가격으로 정하고
        pt = i[0] # 포인트 표시
        price = min(price, i[1]) # 기존 가격과 비교
    else: # 특정 포인트 뒤에 것들은 최소값으로 표시
        check_pt[i[0]] = price
for i in range(n-1):
   oil_l += (distances[i] * check_pt[i])

print(oil_l)
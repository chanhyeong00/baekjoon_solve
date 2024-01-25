from sys import stdin

def find_distance(x,y, num):
    if num == m: # 만약 치킨집 개수가 m과 같아지면 치킨 거리 계산
        min_dis = 0
        for h in house:
            dis = float('inf')
            for c in chicken:
                dis = min(dis,abs(h[0]-c[0]) + abs(h[1]-c[1]))
            min_dis += dis 
        answer.append(min_dis)
        return 
      
    for i in range(x, n): # 반복문으로 치킨집 찾기
        for j in range(y if i==x else 0, n):
            if city[i][j] == 2 and (i,j) not in chicken: #치킨집을 찾아서
                chicken.append((i,j))
                find_distance(i, j, num + 1)
                chicken.pop()

n, m = map(int, stdin.readline().split())
city = []
chicken = []
answer = []
house = []
for _ in range(n):
    street = list(map(int, stdin.readline().split()))
    city.append(street)

for i in range(n): # 집 위치를 미리 계산
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))


find_distance(0,0,0)
print(min(answer))
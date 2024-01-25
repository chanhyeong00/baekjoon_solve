from sys import stdin

def find_distance(x,y, num):
    min_dis = 0
    if num == m: # 만약 치킨집 개수가 m과 같아지면 치킨 거리 계산
        for i in range(n):
            for j in range(n):
                dis = 200000000
                if city[i][j] == 1:
                    for c in chicken:
                        dis = min(dis,abs(i-c[0]) + abs(j-c[1]))
                    min_dis += dis 
        answer.append(min_dis)
        return   
    for i in range(x, n): # 반복문으로 치킨집 찾기(이미 본 곳은 치킨집 없음)
        for j in range(n):
            if city[i][j] == 2 and (i,j) not in chicken: #치킨집을 찾아서
                chicken.append((i,j))
                find_distance(i, j, num + 1)
                chicken.pop()

n, m = map(int, stdin.readline().split())
city = []
chicken = []
answer = []
for _ in range(n):
    street = list(map(int, stdin.readline().split()))
    city.append(street)
find_distance(0,0,0)
print(min(answer))
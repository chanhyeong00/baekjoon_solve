from sys import stdin

n = int(stdin.readline())
house = []
rgb = [[0]*3 for _ in range(n)] 
# rgb 구성은 r[0] ~ r[n], g[0] ~ g[n], b[0] ~ b[n]
# r[n], g[n], b[n] 뜻은 n번째 색을 r or g or b 로 고정하고 이전 색들을 칠한 값들 중 최소값과 더함
# r[n] = min(g[n-1], b[n-1]) + r(마지막 집)
# g[n] = min(r[n-1], b[n-1]) + g(마지막 집)
# b[n] = min(g[n-1], r[n-1]) + b(마지막 집)
# f[n] = min(r[n], g[n], c[n]) 

for _ in range(n):
    house.append(list(map(int, stdin.readline().split())))

for i in range(n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + house[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + house[i][1]
    rgb[i][2] = min(rgb[i-1][1], rgb[i-1][0]) + house[i][2]

print(min(rgb[n-1]))    

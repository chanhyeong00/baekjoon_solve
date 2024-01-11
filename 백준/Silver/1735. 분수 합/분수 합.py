def gcd(x, y):
    while y: # 나머지가 0일 떄까지
        x, y = y, x % y
    return x

a, b = map(int, input().split())
c, d = map(int, input().split())
# (a * d + b * c) 와 b * d 의 최대공약수를 구해서 나눠줌
e = (a * d + b * c)
f = (b * d)
k = gcd(e, f)

print(int(e / k), int(f / k))

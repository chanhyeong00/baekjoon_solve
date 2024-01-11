n = int(input())
gap = []
answer = 0
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
b = int(input())
for i in range(n -1):
    a = int(input())    
    gap.append(a - b)   
    b = a

max_n = gap[0]
for j in range(1, len(gap)):
    max_n = gcd(max_n, gap[j])
for g in gap:
    answer += ((g // max_n) - 1)

print(answer)
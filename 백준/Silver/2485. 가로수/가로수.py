n = int(input())
lst = []
max_n = 1
answer = 0
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

for i in range(n):
    a = int(input())
    lst.append(a)
    if i == 1:
        max_n = a - b
    elif i > 1:
        max_n = gcd(max_n, a - b)
    b = a
for idx, l in enumerate(lst):
    if idx < len(lst)-1:
        diff = lst[idx + 1] - l
        answer += int((diff / max_n) - 1)
print(answer)
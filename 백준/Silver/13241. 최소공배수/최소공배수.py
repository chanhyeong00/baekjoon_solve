a, b = map(int, input().split())

max_num = min(a,b)
while max_num > 1:
    if a % max_num == 0 and b % max_num == 0:
        break
    max_num -= 1

print(int((a * b) / max_num))
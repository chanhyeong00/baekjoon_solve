from sys import stdin

input = stdin.readline

a, b, c = map(int, input().split())

bin_b = bin(b)[2:]
l = 0
answer = 1

base = a % c  # a를 한 번만 계산하여 중복 계산을 방지

for i in range(len(bin_b)-1, -1, -1):
    if bin_b[i] == '1':
        answer = (answer * base) % c
    base = (base * base) % c
    l += 1
print(answer)

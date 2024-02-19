from sys import stdin

input = stdin.readline

a, b, c = map(int, input().split())

def multi(a, divide):
    if divide == 1: # 거듭제곱 1
        return a % c
    else: # 아니면
        part_num = multi(a, divide//2)
        if divide % 2 == 0: # 2의 거듭제곱이면
            return (part_num **2) % c
        else:
            return (part_num ** 2 * a) % c

print(multi(a, b))

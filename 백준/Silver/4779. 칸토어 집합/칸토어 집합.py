from sys import stdin

def cantorian(n):
    if n == 1: # 길이가 1이 된 경우
        return '-'
    else: # 아니면 3등분
        return cantorian(n // 3) + ' ' * (n // 3) + cantorian(n // 3)
while True:
    try:
        n = int(stdin.readline())
        print(cantorian(3**n))
    except:
        break
from sys import stdin

def cantorian(start, n):

    if n == 1: # 길이가 1이 되면
        return
    for i in range(start + n//3, start + n//3 * 2):
        answer[i] = ' '
    cantorian(start, n // 3)
    cantorian(start + n // 3 * 2, n//3)

while True:
    try: # 입력값 없으면 탈출
        n = int(stdin.readline())
        answer = ['-'] * (3**n)
        cantorian(0, 3**n)
        print(''.join(answer))
    except:
        break
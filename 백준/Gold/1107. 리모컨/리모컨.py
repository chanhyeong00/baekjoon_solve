from sys import stdin
input = stdin.readline

def check(num): # 가능한 번호 찾기
    for n in num:
        if int(n) in disable:
            return False
    return True

N = input().strip()
M = int(input())

if M != 0:
    disable = set(map(int, input().split()))
else:
    disable = set()

start = 100
answer = abs(start - int(N))

for channel in range(1_000_001):
    if check(str(channel)):
        answer = min(answer, abs(int(N) - channel) + len(str(channel)))
print(answer)
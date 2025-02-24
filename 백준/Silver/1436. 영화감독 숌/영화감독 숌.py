import sys
input = sys.stdin.readline

N = int(input())
num = 1
k = 666

while True:
    if num == N:
        break
    k += 1
    if '666' in str(k):
        num += 1
print(k)
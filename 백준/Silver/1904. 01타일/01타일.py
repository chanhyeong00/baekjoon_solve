from sys import stdin

n = int(stdin.readline())

mem = [0] * (n+2)

mem[1], mem[2] = 1, 2
for i in range(3, n+1):
    mem[i] = (mem[i-1] + mem[i-2]) % 15746
print(mem[n])
# n = 1, 1
# n = 2, 2
# n = 3, 3
# n= 4 , 5
# n = 5, 7
# n = 6 , 13
# 피보나치
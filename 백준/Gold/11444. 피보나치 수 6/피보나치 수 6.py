from sys import stdin

input = stdin.readline
mod = 1_000_000_007
n = int(input())

mem = {0:0, 1:1, 2:1}
def fib(n):
    if n in mem:
        return mem[n] 
    else:
        if n % 2 == 0:
            result = (fib(n//2) * (fib(n//2) + 2 * fib(n//2 - 1))) % mod
            mem[n] = result 
            return result
        else:
            result = (fib(n // 2 + 1) ** 2 + fib(n//2) ** 2) % mod
            mem[n] = result
            return result
print(fib(n)%mod)
from sys import stdin

input = stdin.readline
mod = 1_000_000_007

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num = (num * i) % mod
    return num

def fast_pow(n, divide):
    if divide == 1:
        return n % mod
    else:
        if divide % 2 == 0: # 거듭제곱이 2의 배수면
            return (fast_pow(n, divide // 2) **2) % mod
        else:
            return (fast_pow(n, divide // 2) **2 * n) % mod

n, r = map(int, input().split())
n_fac = factorial(n)
nr_fac = factorial(n-r)
r_fac = factorial(r)
print((n_fac * fast_pow(nr_fac, mod-2) * fast_pow(r_fac, mod-2))%mod)
# 페르마의 소정리로 정리한 식

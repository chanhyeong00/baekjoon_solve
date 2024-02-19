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

n, k = map(int, input().split())
n_fac = factorial(n)
nk_fac = factorial(n-k)
k_fac = factorial(k)
print((n_fac * fast_pow(nk_fac, mod-2) * fast_pow(k_fac, mod-2))%mod)
# 페르마의 소정리로 정리한 식


# (A+B) % p = ((A%p) + (B%p)) % p
# (A-B) % p = ((A%p) - (B%p) + p) % p
# (A*B) % p = ((A%p) * (B%p)) % p
# 가 모두 성립하지만 나눗셈에는 분배법칙이 성립하지 않으므로
# 조합 공식을 곱셈으로 이어준다

# mod는 나머지 연산을 나타냄

# a!=0, a가 p의 배수가 아니면서 p가 소수일때
#  a^p 를 p로 나눈 나머지는 a를 p로 나눈 나머지와 같다
# a^p ≡ a(mod p) (합동)

# 양변을 a^2으로 나누면
# a^(p-2) = 1/a (mod p)
# 이것을 조합 공식에 사용
# 1.( n! / ( ( n-k )! k! ) )% p 
# 2. (n! * ( ( n-k )! k! )^-1 ) % p 

# 3. a=(( n-k )! k!)로 치환(보기 편하게)
# 4. (n! * a^-1) % p 에서 
# 5. (n! % p) * (a^-1 % p)이고 (분배법칙)
# 6. 위의 식 a^(p-2) = 1/a (mod p) 사용하면
# 7. a^-1 % p = (1/a) % p = a^(p-2) % p 이므로 
# 8. (n! % p) * (a^(p-2) % p) 를 구하면된다
# 9. a = (n-k)! * k! 이므로
# 10. 최종적으로 
# (n! % p) * ( ( ( n-k )!^( p-2 ) ) % p ) * (k!^(p-2) % p)


# 즉 이 문제에선 nlog(p-2)(factorial * pow) 만큼의 시간복잡도가 사용되므로 빠름

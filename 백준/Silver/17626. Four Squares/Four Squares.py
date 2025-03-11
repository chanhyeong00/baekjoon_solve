import sys
input = sys.stdin.readline

N = int(input())
# 모든 수는 4개 이하는 제곱근으로 이루어질 수 있다는 걸 생각하자
def find_min(n):
    if n ** 0.5 == int(n**0.5): 
        return 1
    for i in range(1, int(n**0.5)+1):
        if int((n - i**2)**0.5) == (n - i**2)**0.5: # 남은 수가 제곱근이면
            return 2
    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int((n-i**2)**0.5)+1):
            if int((n - i**2 - j**2)**0.5) == (n - i**2 - j**2)**0.5:
                return 3
    return 4
print(find_min(N))

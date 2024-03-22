
# 비둘기집 원리(Pigeonhole Principle)는 수학적 원리 중 하나로
# 간단히 말해 "너무 많은 물건을 너무 적은 자리에 넣으려고 하면 중복이 발생한다"는 것을 설명합니다.
# 이 원리는 다음과 같이 요약될 수 있습니다:

# 만약 'n' 개의 비둘기가 'm' 개의 비둘기집에 들어가야 한다면, 
# 'n'이 'm'보다 크다면 최소한 하나의 비둘기집에는 두 개 이상의 비둘기가 들어갑니다.

#이것은 간단한 아이디어로, 예를 들어 10마리의 비둘기가 9개의 비둘기집에 들어가야 한다고 가정해 봅시다. 
#이 때, 최소한 한 비둘기집에는 두 마리 이상의 비둘기가 들어가야 합니다. 
#왜냐하면 10마리의 비둘기를 9개의 집에 넣으려고 하면 적어도 한 집에는 두 마리 이상의 비둘기가 들어가야 합니다.

# 중복되는 경우를 생각해서 빠르게 탐색이 가능하다.

from sys import stdin
input = stdin.readline

T = int(input())

def comp(a, b):
    r = 0
    for i in range(4):
        if lst[a][i] != lst[b][i]:
            r += 1
    return r

for _ in range(T):
    N = int(input())
    lst = list(map(str, input().split())) # 최대 16개 나옴
    if N > 32: 
    # 32 이상이면 16개 엠비티아이가 무조건 2개씩은 나오고(16가지 mbti) 
    # 거기서 1개가 들어오면 적어도 하나의 엠비티아이는 3개가 되어서 
    # 심리적 거리는 0이 된다.
        print(0)
    else:
        answer = 1000
        # 더 많은 경우는 탐색을 해보면 된다.
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1, N):
                    result = 0
                    result += comp(i, j)
                    result += comp(j, k)
                    result += comp(k, i)
                    answer = min(answer, result)
        print(answer)

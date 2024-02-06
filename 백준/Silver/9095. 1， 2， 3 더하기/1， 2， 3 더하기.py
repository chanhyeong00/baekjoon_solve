from sys import stdin
read = stdin.readline

def devide(num):
    if num == 0 or num == 1: # 끝까지 도달
        return 1
    if num == 2: # 2면 2가지로 나눠짐(1+1, 2)
        return 2
    if dp[num] != -1: # 이미 값 있으면 있는 값 씀
        return dp[num]
    else: # 3부터는 3가지
        dp[num] = devide(num-1) + devide(num-2) + devide(num-3)

    return dp[num]
    

t = int(read())
for _ in range(t):
    num = int(read())
    dp = [-1] * (num+1)
    dp
    result = devide(num)
    print(result)


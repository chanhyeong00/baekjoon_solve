from sys import stdin

input = stdin.readline

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input())
result = list(str(factorial(n)))

answer = 0
for i in range(len(result)-1, -1, -1):
    if result[i] == '0':
        answer += 1
    else:
        break
print(answer)

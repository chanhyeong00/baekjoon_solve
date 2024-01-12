k = int(input())
lst = []
answer = 0

for _ in range(k):
    num = int(input())
    if num != 0:
        lst.append(num)
        answer += num
    else:
        answer -= lst[-1]
        lst.pop(-1)
print(answer)
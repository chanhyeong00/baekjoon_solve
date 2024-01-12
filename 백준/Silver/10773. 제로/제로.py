k = int(input())
lst = []
answer = 0
prev_num = -1
for _ in range(k):
    num = int(input())
    if num != 0:
        lst.append(num)
    else:
        lst.pop(-1)

print(sum(lst))
m, n = map(int, input().split())

for num in range(m, n+1):
    flag = True
    if num == 1:
        continue
    for j in range(2,int(num**0.5)+1):
        if num % j == 0:
            flag = False
            break
    if flag == True:
        print(num)
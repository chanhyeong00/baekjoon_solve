n = int(input())
comp = abs(n - (len(str(n))*9)) # n이 0~9면 음수 나옴
while True:
    if n // 10 ==0: # 1의자리면 본인 출력
        if n % 2 == 0:
            print(n // 2)
            break
        else:
            print(0)
            break
    if comp == n:
        print(0)
        break
    a = sum(map(int, str(comp))) # 각 자릿수 더하기
    if comp + a == n:
        print(comp)
        break
    comp += 1
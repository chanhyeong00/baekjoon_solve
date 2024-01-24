from sys import stdin

def back(operator, k, result, answer):
    if sum(operator) <= 0: # 연산자 모두 쓰면 출력 후 탈출
        answer.append(result)
        return
    for j in range(4): # 하나씩 본다(연산자를)
        if operator[j] > 0:
            if j == 0:
                operator[j] -= 1
                back(operator, k+1, result+a_lst[k], answer)
                operator[j] += 1
            if j == 1:
                operator[j] -= 1
                back(operator,k+1,result-a_lst[k], answer)
                operator[j] += 1
            if j == 2:
                operator[j] -= 1
                back(operator, k+1,result*a_lst[k], answer)
                operator[j] += 1
            if j == 3:
                operator[j] -= 1
                if result < 0 and a_lst[k] > 0:
                    back(operator, k+1,-(-result//a_lst[k]), answer)
                else:
                    back(operator, k+1,result//a_lst[k], answer)
                operator[j] += 1 
n = int(stdin.readline())

a_lst = list(map(int, stdin.readline().split()))
operator = list(map(int, stdin.readline().split()))

answer = []
back(operator, 1, a_lst[0], answer)

print(max(answer))
print(min(answer))
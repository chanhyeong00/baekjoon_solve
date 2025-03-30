import sys
input = sys.stdin.readline

eq = input().strip('\n')
cnt, answer = 0, 0
minus_on = -1

# 55 +  0 1 2     cnt == 2 -> 2 - 2 : 2-1
for i in range(len(eq)):
    cnt += 1
    if  i == len(eq) - 1:
        if minus_on == 1:
            answer -= int(eq[i-cnt+1:i+1])
        else:
            answer += int(eq[i-cnt+1:i+1])
    if eq[i] == '-' or eq[i] == '+':
        if minus_on == -1:
            if eq[i] == '-': 
                minus_on = 1
            answer += int(eq[i-(cnt-1):i])

        else:
            answer -= int(eq[i-(cnt-1):i])
        cnt = 0
 
print(answer)
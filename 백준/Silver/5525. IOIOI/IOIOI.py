from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
S = input()

pattern = "IOI"

answer = 0
num_pat = 0
end = m
for i in range(m-2): #패턴 IOI이므로 3칸씩 봄

    if end < i: # 패턴 아예 사라짐
        num_pat = 0

    if S[i:i+3] == pattern: # 패턴이 있다면
        end = i+2
        num_pat += 1 # 부분패턴 개수 세고
        if num_pat == n: # 원하는 길이라면
            answer += 1 #정답
            num_pat -= 1 # 앞의 IO 패턴 하나를 줄인다.

print(answer)

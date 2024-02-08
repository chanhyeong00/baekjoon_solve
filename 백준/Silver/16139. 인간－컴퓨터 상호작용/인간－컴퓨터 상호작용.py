from sys import stdin
read = stdin.readline

s = read().strip()
q = int(read()) # a는 고정 알파벳
table = [1] * len(s) # 특정 인덱스까지의 a의 개수

dict_ = {}

# 누적합 미리 구하기
for i in range(len(s)):
    if s[i] not in dict_: # 처음 나온 애면
        dict_[s[i]] = [i]
    else:
        dict_[s[i]].append(i)

for i in range(q):
    a, l, r = map(str, read().split())
    cnt = 0
    if a in dict_:
        for d in dict_[a]:
            if d >= int(l) and d <= int(r):
                cnt += 1
    print(cnt)
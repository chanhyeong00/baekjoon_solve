from sys import stdin
read = stdin.readline

s = read().strip()
q = int(read()) # a는 고정 알파벳

# 알파벳마다 별도의 누적 합 배열 초기화(아스키코드 사용(97~122))
dict_ = {chr(i): [0] * (len(s) + 1) for i in range(97, 123)}

for i in range(1, len(s)+1):
    for key in dict_:
        if s[i - 1] == key:
            dict_[key][i] = dict_[key][i-1] + 1
        else:
            dict_[key][i] = dict_[key][i-1]

for i in range(q):
    a, l, r = map(str, read().split())
    l, r = int(l), int(r)

    print(dict_[a][r+1] - dict_[a][l])

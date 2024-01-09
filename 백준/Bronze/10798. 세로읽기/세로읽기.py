max_l = 0

lst = [''] * 15 # 순서별로 정리된 글자 (최대 길이 15)
for _ in range(5):
    s = input()
    for i, l in enumerate(lst): # i는 
        if i <= len(s) - 1:
            lst[i] += s[i]
answer = ''.join(lst)
print(answer)
    

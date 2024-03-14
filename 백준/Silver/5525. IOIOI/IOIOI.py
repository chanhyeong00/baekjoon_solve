from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

S = input()
n_p = 2 * n + 1

answer = 0
change = {'I':'O', 'O':'I'}
for i in range(m):
    k = i
    if S[i] == 'I':
        curr = 'I'
        if i+n_p -1 < m:
            for j in range(i+n_p -1, -1, -1):
                if k == j and S[k] == S[j] and S[k]==curr:
                    answer += 1
                    break
                if S[k] != S[j] or curr != S[k]:
                    break       
                curr = change[curr] 
                k += 1
print(answer)
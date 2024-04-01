from sys import stdin
input = stdin.readline

def change(r):
    return not r
def remove(r, f, b):
    if not r:
        f += 1
    else:
        b += 1
    return f, b

def make_answer(r, f, b):
    answer = []
    cnt = 0
    if r == False:
        for i in range(f, len(arr)-b):
            answer.append(arr[i])
    else:
        for i in range(len(arr)-1-b, -1+f, -1):
            answer.append(arr[i])
    return answer

def change_str(ans):
    answer = '['
    for idx, a in enumerate(ans):
        answer += a
        if idx < len(ans) - 1:
            answer += ','
    return answer + ']'
        
T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()

    if n > 0:
        arr = list(arr[1:-1].split(','))
    else:
        arr = []
    l = len(arr)

    front_d = 0 # 앞에 삭제 목록
    back_d = 0 # 뒤에 삭제 목록
    state = False 
    for i in p:
        if i == 'R':
            state = change(state)               
        else:
            l -= 1
            front_d, back_d = remove(state, front_d, back_d) 
    answer = make_answer(state, front_d, back_d)
    if l < 0:
        print('error')
    else:
        print(change_str(answer))
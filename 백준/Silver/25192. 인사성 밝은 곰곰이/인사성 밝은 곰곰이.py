from sys import stdin
n = int(stdin.readline())

chat_lst = set()
answer = 0
for i in range(n):
     who = stdin.readline().strip()
     if who == 'ENTER': # 기록 시작
          answer += len(chat_lst)
          chat_lst.clear()
     else:
          chat_lst.add(who)
          if i == n - 1:
               answer += len(chat_lst)
print(answer)
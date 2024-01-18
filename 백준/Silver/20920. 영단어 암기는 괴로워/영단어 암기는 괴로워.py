from sys import stdin
n, m = map(int, stdin.readline().split())
note = {}

for _ in range(n):
     word = stdin.readline().strip()
     if len(word) >= m:
          if word not in note:
               note[word] = 1
          else:
              note[word] += 1

answer = list(note.items())

answer.sort(key=lambda x : x[0])
answer.sort(key=lambda x : len(x[0]), reverse=True)
answer.sort(key=lambda x: x[1], reverse=True)

for a in answer:
     print(a[0])
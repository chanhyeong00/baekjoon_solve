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
# 하나씩 풀어쓸 땐 우선순위 가장 낮은 애부터 sort
answer.sort(key=lambda x : x[0])
answer.sort(key=lambda x : len(x[0]), reverse=True)
answer.sort(key=lambda x: x[1], reverse=True)

#answer.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
# 한번에 쓰는 것도 가능(우선순위 순서대로)
for a in answer:
     print(a[0])

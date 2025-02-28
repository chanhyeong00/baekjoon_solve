import sys
n, m = map(int, sys.stdin.readline().split())
name = {}
lst = []
cnt = 0
for _ in range(n):
    no_lsn = sys.stdin.readline().strip()
    name[no_lsn] = 0
for _ in range(m):
    no_see = sys.stdin.readline().strip()
    if no_see in name:
        name[no_see] += 1
        cnt += 1
        lst.append(no_see)
print(cnt)
for l in sorted(lst):
    print(l)

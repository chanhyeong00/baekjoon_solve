from sys import stdin
read = stdin.readline

n = int(read())
time = list(map(int, read().split()))
total_time = [0] * (n+1)

time.sort()

for i in range(1, n+1):
    total_time[i] = total_time[i-1] + time[i-1] 
print(sum(total_time))


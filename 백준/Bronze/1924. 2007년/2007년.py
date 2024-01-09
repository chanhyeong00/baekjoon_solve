x, y = map(int, input().split())

lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
day = 0

for d in range(x - 1): # 3이면 1 2 만(0 1 까지만)
    day += lst[d]

day += (y - 1) # 남은 날짜 더하기    
day %= 7

print(date[day])
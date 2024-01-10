a, b, c, d, e, f, = map(int, input().split())
x, y = 0, 0
flag = False
for x1 in range(1000):
    for y1 in range(1000):
        if a*x1 + y1 * b == c and d* x1 + e * y1 == f:
            x = x1
            y = y1
            flag = True
            break
        elif -a*x1 + y1 * b == c and -d* x1 + e * y1 == f:
            x = -x1
            y = y1
            flag = True
            break
        elif a*x1 - y1 * b == c and d* x1 - e * y1 == f:
            x = x1
            y = -y1
            flag = True
            break
        elif -a*x1 - y1 * b == c and -d* x1 - e * y1 == f:
            x = -x1
            y = -y1
            flag = True
            break
    if flag == True: break
print(x, y)
from sys import stdin
read = stdin.readline
   
t = int(read())

dp_z = [0] * 41
dp_o = [0] * 41

dp_z[0], dp_z[1], dp_z[2], dp_z[3] = 1, 0, 1, 1
dp_o[0], dp_o[1], dp_o[2], dp_o[3] = 0, 1, 1, 2

for _ in range(t):
    n = int(read())
    if n < 4:
        print(dp_z[n], dp_o[n])
    else:
        for i in range(4, n+1):
            dp_z[i] = dp_z[i-1] + dp_z[i-2]
            dp_o[i] = dp_o[i-1] + dp_o[i-2] 
        print(dp_z[n], dp_o[n])
        

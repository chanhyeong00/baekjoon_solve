from sys import stdin

def w(a, b, c):
    result = float('inf')
    if (a,b,c) in dict_:
        return dict_[(a,b,c)]
    if a <= 0 or b <= 0 or c <= 0:
        dict_[(a,b,c)] = 1
        return dict_[(a,b,c)]
    if a > 20 or b > 20 or c > 20:
            dict_[(a,b,c)] = w(20, 20, 20)
            return dict_[(a,b,c)]
    if a < b and b < c:
        dict_[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dict_[(a,b,c)]
    else:
        dict_[(a,b,c)]= w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dict_[(a,b,c)]
    
dict_ = {}
while True:
    a, b, c = map(int, stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({0}, {1}, {2}) = {3}'.format(a, b, c, w(a,b,c)))
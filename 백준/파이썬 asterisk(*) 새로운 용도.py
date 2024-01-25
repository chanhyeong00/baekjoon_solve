lst = [1,2,3,4,5,6,7]
print(*lst)

a, *b = lst
print(a, b)

a, b, c, *d = lst
print(a,b,c,d)

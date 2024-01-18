def fibonach(n):
    result = 0
    if n == 0:
        result = 0
    if n == 1:
        result = 1 
    else:    
        if n > 1:
            result = fibonach(n-1) + fibonach(n-2)
    return result
n = int(input())
print(fibonach(n))
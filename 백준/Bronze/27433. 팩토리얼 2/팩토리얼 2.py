from sys import stdin

def factorial(n):
     num = n

     if n == 1 or n == 0:
          return 1
     else:
          num *= factorial(n-1)

     return num

n = int(stdin.readline())
print(factorial(n))
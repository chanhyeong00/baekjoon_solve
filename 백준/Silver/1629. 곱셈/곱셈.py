from sys import stdin

input = stdin.readline

a, b, c = map(int, input().split())

print(pow(a,b,c))
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)
answer = 0

while start <= end:
    cut_size = (start + end) // 2 # 절단기 높이
    len_tree = 0 # 잘려나간 나무 길이
    for t in tree:
        if t > cut_size: # 나무 높이가 절단기 높이보다 높으면 잘림
            len_tree += (t - cut_size) 
    if len_tree >= m: # 잘려나간 길이가 원하는 길이보다 같거나 많다면(적어도)
        answer = max(answer, cut_size) # 가능
        start = cut_size + 1 # 절단기 높이 높혀봄
    else: # 적다면 -> 절단기 높이를 낮춰서 더 많이 자름
        end = cut_size - 1 

print(answer)
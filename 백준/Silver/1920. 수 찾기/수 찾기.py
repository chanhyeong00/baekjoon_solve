from sys import stdin
n = int(stdin.readline())
a_lst = list(map(int, stdin.readline().split()))
a_lst.sort()
m = int(stdin.readline())
b_lst = list(map(int, stdin.readline().split()))

def bin_s(x, lst):
     start = 0
     end = len(lst) - 1
     answer = 0
     while start <= end:
          mid = (start + end) // 2

          if x == lst[mid]:
               answer = 1
               break
          elif lst[mid] > x:
               end = mid -1 
          else:
               start = mid + 1   
     return answer

for b in b_lst:
     print(bin_s(b, a_lst))
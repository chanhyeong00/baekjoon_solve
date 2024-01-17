from sys import stdin
n = int(stdin.readline())
a_lst = sorted(list(map(int, stdin.readline().split())))
a_lst.sort()

m = int(stdin.readline())
b_lst = list(map(int, stdin.readline().split()))

for b in b_lst:
     start = 0
     end = len(a_lst) - 1
     flag = False
     while start <= end:
          mid = (start + end) // 2

          if b == a_lst[mid]:
               flag = True
               print(1)
               break
          elif a_lst[mid] > b:
               end = mid -1 
          else:
               start = mid + 1
     
     if flag == False: print(0)

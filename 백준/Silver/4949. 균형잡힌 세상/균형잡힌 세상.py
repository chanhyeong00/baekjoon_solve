from sys import stdin

while True:
     open_state = []# 0은 소괄호, 1은 대괄호
     sen = stdin.readline().replace("\n", "")
     if sen == '.':
          break
     for s in sen:
          if s == '(': # 열었음
               open_state.append(')')
          elif s == '[':
               open_state.append(']')
          elif s == ')' or s == ']':
               if not open_state:
                    open_state.append('fail')
                    break
               else:
                    if open_state[-1] == s:
                         open_state.pop(-1)
                    else:
                         break
     if len(open_state) == 0:
          print('yes')
     else:
          print('no')
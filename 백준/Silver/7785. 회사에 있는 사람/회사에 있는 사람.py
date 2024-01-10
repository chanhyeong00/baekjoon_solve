n = int(input())
_dict = {}
lst = []
for _ in range(n):
    name, state = map(str, input().split())
    _dict[name] = state
for name, state in sorted(_dict.items(), reverse=True):
    if state == "enter":
        print(name)
     

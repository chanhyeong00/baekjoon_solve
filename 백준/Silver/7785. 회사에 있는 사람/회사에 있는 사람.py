n = int(input())
_dict = {}
lst = []
for _ in range(n):
    name, state = map(str, input().split())
    _dict[name] = state
for name, state in _dict.items():
    if state == "enter":
        lst.append(name)
lst.sort(reverse=True)
for l in lst:
    print(l)

    



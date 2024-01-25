visited = [False for _ in range(n)]
arr = []


def make_arr(k, n, m):
    if k == m: # 일정 깊이에 도착하면 동작 후 리턴
        print(' '.join(map(str, arr)))
        return
    for i in range(len(visited)): # 이 부분에서 탐색시작 지점을 잡고 시간복잡도를 줄이는 게 관건.
        if not visited[i]:
            visited[i] = True # 방문함을 표시
            arr.append(i+1) 
            make_arr(k+1, n, m) # 백트레킹
            visited[i] = False # 탐색끝
            arr.pop()


make_arr(0, n, m)

# BFS는 너비 방향으로 탐색을 진행하는 알고리즘입니다. 큐(queue)를 사용하여 구현하는 것이 일반적이다

from collections import deque

def bfs(graph, start): # 시작점을 기점으로 시작
    visited = set() # 방문했는지 여부
    queue = deque([start]) # 갈 수 있는 인접 노드를 표시해주는 큐

    while queue: # 큐가 비어있지 않다면 반복
        node = queue.popleft() # 큐의 왼쪽(가장 먼저 들어온 애)을 팝해서 현재 노드로 설정
        if node not in visited: # 방문 여부에 노드가 없으면
            visited.add(node) # 방문 했음을 표시하기 위해 추가
            print(node, end=' ') # 방문한 노드 출력

            for neighbor in graph[node]: # 그 노드의 인접노드를 살핌
                if neighbor not in visited: # 방문 안했다면
                    queue.append(neighbor) # 큐에 넣는다

# 예시 그래프
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

bfs(graph, 'A')

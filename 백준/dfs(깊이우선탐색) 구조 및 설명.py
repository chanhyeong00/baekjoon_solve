# DFS는 깊이 방향으로 탐색을 진행하는 알고리즘입니다. 재귀 함수나 스택(stack)을 사용하여 구현할 수 있다

# 재귀
def dfs_recur(graph, node, visited):
    if node not in visited: # 
        print(node, end=' ')
        visited.add(node)

        for neighbor in graph[node]:
            dfs_recur(graph, neighbor, visited)
# 스택
def dfs_stack(graph, start):
    visited = set()  # 방문한 노드를 기록하기 위한 집합
    stack = [start]  # 스택을 초기화하고 시작 노드를 넣음

    while stack: # 스택이 차있는 동안
        node = stack.pop()  # 스택에서 노드를 꺼내옴
        if node not in visited: # 만약 노드가 방문하지 않은 노드라면
            print(node, end=' ') # 동작 후
            visited.add(node) # 방문했다는 것을 알림

            # 현재 노드의 인접한 노드들을 스택에 추가
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# 예시 그래프 A B D E H C F G %  
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
visited = set()
dfs_stack(graph, 'A')
print()
visited.clear()
dfs_recur(graph, 'A', visited)

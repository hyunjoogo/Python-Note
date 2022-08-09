###########  DFS  ###########

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
# 노드의 값과 같게 하기 위해 0번째 인덱스를 비워두었다.
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# 그래프에서 0번째 인덱스를 비워둔 것처럼 편하게 관리하기 위해 0번째 인덱스는 사용하지 않는다.
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

###########  BFS  ###########
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False] * 9
bfs(graph, 1, visited)


# 간단정리
#                DFS            BFS
# 동작원리      스택         / 큐
# 구현방법      재귀 함수 이용 / 큐 자료구조 이용
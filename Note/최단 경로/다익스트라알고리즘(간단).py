import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


# 방문하지 않은 노드중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        '''처음 호출할 때 => 1번째 인덱스가 방문한 노드이므로 if문을 타지 않는다'''
        print(distance[i], visited[i], end=' ')
        if distance[i] < min_value and not visited[i]:
            ''' 거리가 같은 노드일 경우 (2, 5번째 노드) min_value가 2번째 노드에서 갱신되었기때문에 
            if문의 < 부등호에 걸려서 아예 안탐 '''
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    # start노드를 거쳐서 j[0] 노드까지 가는 최소비용(j[1]) 대입하기
    for j in graph[start]:
        # (2, 2), (3, 5), (4, 1)
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        print('i', i, distance, now)
        ''' i는 0 ~ 4까지
        i = 0일 때 now == 4 -> 2번 노드 : 최단 2 / 3번 노드 : 최단 5 / 4번 노드 : 최단 1
        i = 1일 때 now == 2 -> 2번 노드 : 최단 2 / 3번 노드 : 최단 4 / 4번 노드 : 방문 / 5번 노드 : 최단 2 (최단 함수 로직으로 제외)
        i = 2일 때 now == 5 -> 2번 노드 : 방문 / 3번 노드 : 최단 4 / 4번 : 방문 / 5번 : 최단 2
        i = 3일 때 now == 3 -> 2번 : 방문 / 3번 : 최단 3 / 4번 : 방문 / 5번 : 방문 / 6번 : 최단 4
        i = 4일 때 now == 6 -> 2번 : 방문 / 3번 : 방문 / 4번 : 방문 / 5번 : 방문 / 6번 : 최단 4
    
        '''
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            ''' 
            i = 0 , now == 4 , j = (3, 3), (5, 1) => 3번 거리, 5번 거리 변경
            i = 1 , now == 2 , j = (3, 3), (4, 2) => 거리 변경 없음
            i = 2일 때 now == 5 , j = (3, 1), (6, 2) => 3번 거리 변경, 6번 거리 변경
            i = 3일 때 now == 3 , j = (2, 3), (6, 5) => 거리 변경 없음
            i = 4일 때 now == 6, j = 없음 => 거리 변경 없음
            '''
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


graphList = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []
]

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

'''
6 11
1 
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

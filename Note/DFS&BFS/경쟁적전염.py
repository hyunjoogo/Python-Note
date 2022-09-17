from collections import deque

n, m = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담은 리스트

for i in range(n):
  # 보드 정보를 한 줄 단위로 입력
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 해당 위치에 바이러스가 존재하는 경우
    if graph[i][j] != 0:
      # (바이러스종류, 시간, 위치 X, 위치 Y) 입력
      data.append((graph[i][j], 0, i, j))
'''바이러스에 대한 정보를 담은 리스트를 따로 만들어서 그 리스트를 BFS로 탐색'''

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)
target_sec, target_x, target_y = map(int, input().split())

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색 (BFS) 진행
while q:
  virus, sec, x, y = q.popleft()
  # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
  if sec == target_sec:
    break
  # 현재 노드에서 주변 4가지 위치를 각각 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 해당 위치로 이동할 수 있는 경우
    if 0 <= nx and nx < n and 0 <= ny and ny < m:
      # 아직 방문하지 않은 위치라면 그 위치에 바이러스 넣기
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, sec + 1, nx, ny))


print(graph[target_x-1][target_y-1])
'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2
'''
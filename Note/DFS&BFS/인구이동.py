from collections import deque

n, l, r = map(int, input().split())

graph = [] # 초기 맵 리스트
for _ in range(n):
  graph.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
  # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
  united = []
  united.append((x, y))
  # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
  queue = deque()
  queue.append((x, y))

  union[x][y] = index # 현재 연합의 번호 할당
  summary = graph[x][y] # 현재 연합의 전체 인구 수
  count = 1 # 현재 연합의 국가 수
  # 큐가 빌 때까지 반복(BFS)
  while queue:
    x, y =  queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # union[nx][ny] == -1 처리를 했는지 알 수 있음
      if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
        # 옆에 있는 나라와 인구 차이가 l명 이상, r명 이하라면
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
          print(nx, ny)
          queue.append((nx, ny))
          # 연합에 추가
          union[nx][ny] = index
          summary += graph[nx][ny]
          count += 1
          united.append((nx, ny))
          print('united', united,'union',  union)
  # 연합 국가끼리 인구를 분해
  for i,j in united:
    graph[i][j] = summary // count
  return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
          # 각 나라를 돌면서 처리되어 있는지 확인
          
          if union[i][j] == -1 :
            process(i, j, index) # 해당 나라가 아직 처리되지 않았다면
            print(i, j, union)
            index += 1
    if index == n * n:
        break
    total_count += 1


print(total_count)
'''
2 20 50
50 30
20 40
'''
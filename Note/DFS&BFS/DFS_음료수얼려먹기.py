# 출구 위치이면
# n줄, m번째
n, m = map(int, input().split())


graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):  # x줄, y번째
    # 주어진 범위를 벗어나면 종료
    if x <= -1 or y <= -1 or x >= m or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우의 값을 방문값으로 바꾸는 작업
        # 정상범위라면 리턴값이 없으므로 방문처리하는데만 쓰임
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)

'''
4 5
00110
00011
11111
00000
'''

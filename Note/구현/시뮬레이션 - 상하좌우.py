# N * N 크기의 정사각형 공간이 있으며, 가장 왼쪽 위 좌표는 (1,1)
# 상, 하, 좌, 우로 이동할 수 있고 시작좌표는 (1,1)
# 입력 받은 계획서에 왼쪽 L, 오른쪽 R, 위 U, 아래 D로 한 칸 이동하며 이동할 수 없는 경우 움직임은 무시된다.

# 최종 도착할 지점의 좌표를 출력하라

# 나의 풀이

# 핵심 키워드 : 시키는 대로 하자

# (1, 1) 좌표를 리스트 인덱스에 맞게 (0, 0)으로 변경
# 계획서를 돌면서 각 영어에 따라 현재 좌표를 움직이게 한다.
# 다만 움직일 수 없는 공간일 경우 움직이지 않는다.


n = int(input())
moveList = input().split()

result = [0, 0]

for move in moveList:
    if move == 'R':
        # 움직일 수 있는 공간인지 확인
        if result[1] + 1 < n:
            result[1] += 1
    elif move == 'L':
        # 움직일 수 있는 공간인지 확인
        if result[1] - 1 > 0:
            result[1] -= 1
    elif move == 'U':
        # 움직일 수 있는 공간인지 확인
        if result[0] - 1 > 0:
            result[0] -= 1
    else:
        # 움직일 수 있는 공간인지 확인
        if result[0] + 1 < n:
            result[0] += 1

print(result[0] + 1, result[1] + 1)

# 다른 문제 풀이
# 입력 문자에 따른 이동 방향을 리스트로 만들기
# 따로 (0, 0)으로 이동시키지 않고 그대로 진행

n = int(input())
x, y = 1, 1
plans = input().split()

# LRUD 입력 문자에 따른 이동 방향을 리스트로 만들기
# 처음에 헷갈렸는데 왼쪽, 오른쪽 이동은 0번째가 아니라 1번째 인덱스가 변경된다.
# 그래서 y가 움직이는 것
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            # 새로운 좌표를 변수로 만들어서 아래 if문을 통과못하면 그래도 무시된다.
            # 즉, nx, ny는 이동가능한지 보기 위해 일시적인 변수이고
            # 이동할 수 있다면 x, y에 할당한다.
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
'''
5
R R R U D D
'''

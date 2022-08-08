# 8방향으로 움직일 수 있다고 생각하고
# 움직인 좌표를 nx, ny로 하고
# 움직인 좌표가 이동범위를 넘어가면 continue
# 움직인 좌표가 이동범위 안이면 count++


# row, column이 자주 헷갈린다.
# row, x 는 가로 , 2차원 배열의 1번째 인덱스에 속한다.
# -> -> -> 옆으로 넘어간다.

# column, y는 세로 , 2차월 배열의 0번째 인덱스에 속한다.
# 아래로 아래로 넘어간다.

# 문제에서 줄 때 (x, y) 형식으로 주는데


# 나의 풀이
transX = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
inputs = input()
x, y = transX[inputs[0]], int(inputs[1])

# dx, dy를 이런식으로도 표현이 가능하다.
move_types = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

count = 0

for move in move_types:
    nx = x + move[0]
    ny = y + move[1]
    # 평면을 벗어나면
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)

# 다른 사람의 풀이
# for문의 if문을 벗어나지 않는다면 이라는 조건으로 바꾸었다.

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a')) + 1)

count = 0

for move in move_types:
    nx = x + move[0]
    ny = y + move[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1
print(count)

# 연구소문제랑 비슷
# 조합 라이브러리 사용


'''
연구소 문제와 비슷
1. 학생이 있는지 없는지를 확인하므로 True/False를 리턴하는 함수가 필요
- watch()함수 내부에서 한 방향의 끝까지 값을 확인하는 것을 while로 구현
- 모두 다 돌았는데 조건에 안맞으면 False, 중간에 학생을 만나면 바로 True, 장애물을 만나면 바로 False
2. 방향을 설정할 때 0~3까지 for 문 이용
- watch() 함수의 인자값으로 넘겨서 if문으로 0, 1, 2, 3일 때 (좌, 우, 상, 하 )를 확인할 수 있음
3. process() 함수는 각 방향을 돌면서 watch() 함수에서 학생이 발견되면 (True) Ture를 리턴
- 없으면 False를 리턴
4. 빈 공간 list에서 3개를 뽑는 조합
- for data in combinations(spaces, 3):
- [((0, 0), (0, 2), (0, 3)), ((0, 0), (0, 2), (1, 1)), ...]
- (0, 0), (0, 2), (0, 3) 좌표에 장애물 '0' 대입


'''

from itertools import combinations

n = int(input())
board = [] # 복도 정보 (N * N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    # 선생님이 존재하는 위치 저장(좌표로)
    if board[i][j] == 'T':
      teachers.append((i,j))
    # 장애물을 설치할 수 있는 위치 저장
    if board[i][j] == 'X':
      spaces.append((i,j))


# 특정 방향으로 감시를 진행(학생 발견: True, 학생 미발견 : False)
# 선생님의 위치에서 상, 하, 좌, 우를 확인하며 학생이 한 명이라도 감지되는지 확인하는 함수
# 장애물을 만나면 미발견으로 바로 종료
def watch(x, y, direction):
  # 왼쪽 방향으로 감시
  if direction == 0:
    while y >= 0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == '0':
        return False
      y -= 1
  # 오른쪽 방향으로 감시
  if direction == 1:
    while y < n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == '0':
        return False
      y += 1
  # 위쪽 방향으로 감시
  if direction == 2:
    while x >= 0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == '0':
        return False
      x -= 1
  # 아래쪽 방향으로 감시
  if direction == 3:
    while x < n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == '0':
        return False
      x += 1
  return False # 모두 다 돌았는데 없다!

# 장애물 설치 이후에, 한명이라도 학생이 감지되는지 검사
def process():
  # 모든 선생님의 위치를 하나씩 확인
  for x, y in teachers:
    # 4가지 방향으로 학생을 감지할 수 있는지 확인
    for i in range(4):
      if watch(x, y, i):
        return True
  return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여우

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
  for x, y in data:
    board[x][y] = '0'
  # 학생이 한 명도 감지 되지 않는 경우
  if not process():
    # 원하는 경우를 발견한 것임 (감지되는 학생이 없다!)
    find = True
    break
  # 원하는 경우가 없으면 설치된 장애물 다시 없애기
  for x, y in data:
    board[x][y] = 'X' 

if find:
  print('YES')
else:
  print('NO')
'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
'''
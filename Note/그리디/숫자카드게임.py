# 뽑고자 하는 행을 선택한다.
# 선택된 행에 포함된 카드들 중 가장 낮은 카드를 뽑아야한다.

# 각 행마다 가장 작은 수를 찾고 그 수 중에 가장 큰 수

# 나의 풀이
# 입력받은 카드들의 값을 오름차순으로 정렬 => 카드 리스트를 만듬
# 각 행을 돌면서 0번째 인덱스를 작은 수 리스트에 넣음
# 그 중 가장 작은 숫자의 인덱스를 출력
n, m = list(map(int, input().split()))
data = []
for _ in range(n):
    temp = list(map(int, input().split()))
    temp.sort()
    data.append(temp)
minNum = []
for i in range(n):
    minNum.append(data[i][0])

print(minNum.index(max(minNum)))

# 다른 사람 풀이
# 입력받은 카드들 중 가장 작은 수를 찾고
# result와 비교
# - 0번째와 1번째 입력때부터 비교가 가능하다.
n, m = list(map(int, input().split()))

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄의 가장 작은 수 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
'''
3 3
3 1 2
4 1 4
2 2 2
'''

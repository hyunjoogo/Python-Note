# 선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

print(array)

# 삽입정렬
# - 첫번째 데이터는 정렬되어 있다고 간주하고 시작 (두 번째 데이터부터 시작)
# - 바로 왼쪽에 있는 데이터보다 작은 경우 왼쪽으로 이동하다가 자신보다 작은 데이터를 만났을 때 그 위치 삽입된다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

# 직관적인 퀵 정렬 소스
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 테이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

# 파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫번째 원소
    tail = array[1:]  # 피벗을 제왼한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))

# 계수 정렬 :
# - 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 : 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')

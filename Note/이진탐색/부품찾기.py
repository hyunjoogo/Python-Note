# 재귀함수를 이용한 이진탐색

def recursion_binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return target
    elif array[mid] > target:
        return recursion_binary_search(array, target, start, mid - 1)
    else:
        return recursion_binary_search(array, target, mid + 1, end)

# 반복문을 이용한 이진탐색
def while_binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = recursion_binary_search(arr, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

for i in x:
    result = while_binary_search(arr, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
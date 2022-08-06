# 주어진 배열의 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 조건1. 특정 인덱스에 해당하는 수가 연속 K번을 더해질 수 없다.
# 조건2. 서로 다른 인덱스에 해당하는 수가 같은 경우 서로 다른 것으로 간주


# 아이디어
# 1. 가장 큰 수를 K번 더하고 한번 작은 수 더하고 그렇게 M번 채우기
# - 1,4,3,5 이면 5를 2번 더하고 5보다 하나 작은 인덱스의 숫자를 더하는 방식
# - 만약 가장 큰 수가 조건2에 해당되면? 그걸 어떻게 알지?
# - 1,4,5,5 이면 서로 다른 것으로 간주한다고 하니까 그냥 더해도 될듯

# 오름차순으로 정렬하고
# 마지막 인덱스의 값을 K번 더하고 마지막 인덱스 -1의 값을 1번 더하고
# 그 와중에 M이 차면 종료

# 나의 풀이
n, m, k = map(int, input().split())
data = sorted(list(map(int, input().split())))

result, count, repeat = 0, 0, 0

while True:
    if count == m:
        break
    if repeat == k:
        result += data[-2]
        repeat = 0
    else:
        result += data[-1]
        repeat += 1
    count += 1
print(n, m, k, data)
print(result)

# 다른 사람 풀이


'''
5 8 3
2 4 5 4 6
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

# m번, k번을 마이너스 하는 방식
# k번 더하는 것을 for문으로 돌리는 것
# for문이 다 돌면 k번을 더한 것이므로 second 더하기
while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # 중간에 m번을 더했으면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    # k번을 더했는데 M번을 더 했을 수도 있으니까 if문으로 빠져나갈 수 있게 한다.
    if m == 0:
        break
    # 여기서 더해서 m이 0이 되면 반복문의 for문의 if문에서 걸려서 탈출된다.
    result += second
    m -= 1

print(result)

# M의 크기가 클 때
# 반복되는 패턴 찾기 : {6, 6, 6, 5} + {6, 6, 6, 5} => 8 = 4 * 2
# 여기서 2번 더해지는 것을 수식으로 구해야한다.
# m / (k+1)의 몫이 더한 횟수가 된다.
# 만약 나누어 떨어지지 않는다면 나머지만큼 가장 큰 수를 더해야한다.

# 가장 큰수를 더하는 횟수를 구해서 더하고
# 두번째 큰 수를 더하는 횟수는 전체 더하는 횟수에서 가장 큰 수를 더하는 횟수를 빼면 된다.

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]
# 가장 큰수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k  # k는 반복횟수, int(m / (k + 1))는 더해지는 횟수
count += m % (k + 1)

result = 0

result += count * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두번째로 큰 수 더하기

print(result)

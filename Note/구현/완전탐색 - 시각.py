# 00시 00분 00초부터 23시 59분 59초가지의 모든 시각 중에서 3이 하나라도 포함되어 있는 경우의 수를 구하여라

# 완전탐색 유형
# - 가능한 경우의 수를 모두 검사해보는 탐색 방법
# - 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색 이용

# 나의 풀이
n = int(input())
hour = n
minute = 60
second = 60
count = 0
for i in range(n + 1):
    for j in range(minute):
        for k in range(second):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                count += 1
print(count)

# 다른 사람 풀이

count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # str(i) + str(j) + str(k) => 55754 이런 식으로 나온다.
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
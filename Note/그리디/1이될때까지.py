# 어떠한 수 N이 1이 될 때까지 반복적으로 수행하려고 한다.
# 1번 과정 : N에서 1을 뺀다
# 2번 과정 : N을 K로 나눈다. (나누어 떨어질 때만 가능)

# 최소 횟수를 구하여라

# 핵심키워드 : 최대한 2번 과정을 사용하라

# 나의 방법

# 과정을 한 번할 때마다 카운터업
# 나누어 떨어진다면 2번 과정
# 나누어 떨어지지 않는다면 1번 과정 반복


# 8 / 3 이라면
# 나누어 떨어지지 않으므로
# 1번 과정을 2번 한다. 8 % 3 이 2이므로

# 아.... 2 % 3일 때는 n이 0으로 된다.
n, k = map(int, input().split())

count = 0
while n == 1:
    if n % k == 0:
        n = n % k
        count += 1
    else:
        repeat = n % k
        n = n - repeat
        count += repeat

# 다른 풀이

result = 0
print(n // k, k, (n // k) * k)
while True:
    # 나누어 떨어질 때까지 1번 과정 반복
    target = (n // k) * k
    result = n - target
    n = target
    print("target", target, n // k, k)
    # n이 k보다 작으면 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n = n // k
print(n)
result += n - 1
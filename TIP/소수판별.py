import math


# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True


print(is_prime_number(4))

# 에라토스테네스의 체 ( 여러 개의 수가 소수인지 아닌지를 판별할 때 사용)
# N보다 작거나 같은 모든 소수를 찾을 때 사용

n = 1000  # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화(0, 1은 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인하며
    # i가 소수인 경우 (남은 수인 경우)
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')

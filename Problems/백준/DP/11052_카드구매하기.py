# https://www.acmicpc.net/problem/11052

n = int(input())

p = list(map(int, input().split()))
p.insert(0, 0)

dp = [0] * 10001


for i in range(1, n + 1):
    for k in range(1, i):
        # 현재 카드와 현재-1카드 + 이전최대값
        print(i, k)
        # 왜 p[i]가 아니라 dp[i]일까
        dp[i] = max(dp[i], dp[i - k] + p[k])
print(dp[i])

# 한장을 사는 최대값
# 1. 본인자신
# 2. i-1 과 i-2를 사는 최대값

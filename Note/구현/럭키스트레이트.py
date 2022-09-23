n = input()
len = len(n)
a = list(map(int, n))

# 인덱스 0(시작) ~ 1(중간) 까지의 합과 2 ~ 3(끝) 까지의 합

print(a[:int(len / 2)], a[int(len / 2):])

if sum(a[:int(len / 2)]) == sum(a[int(len / 2):]) :
  print('LUCKY')
else:
  print('READY')


summary = 0
# 왼쪽 부분의 자릿수 합 더하기
for i in range(len // 2):
  summary += int(n[i])

# 오른족 부분의 자릿수 합 빼기
for i in range(len // 2, len):
  summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
  print('LUCKY')
else:
  print('READY')

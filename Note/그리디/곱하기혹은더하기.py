# 0 * ?는 안되
# 0일 때는 +
# 나머지는 곱하기


n = input()

result = int(n[0])
for i in range(1, len(n)):
    now = int(n[i])
    if now == 0:
        continue
    else:
        if result == 0:
            result += now
        else:
            result = result * now

print(result)

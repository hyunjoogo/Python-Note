n = int(input())
data = list(map(int, input().split()))

data.sort()

target = 1
for x in data:
    print(target, x)
    if target < x:
        break
    target += x

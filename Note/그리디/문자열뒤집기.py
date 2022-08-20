s = input()

zero = 0
one = 0


if s[0] == '0':
    zero += 1
else:
    one += 1

for i in range(len(s) - 1):
    # 현재 문자가 이전 문자와 다른 경우,
    if s[i] != s[i + 1]:
        if s[i + 1] == '0':
            one += 1
        else:
            zero += 1


print(min(zero, one))

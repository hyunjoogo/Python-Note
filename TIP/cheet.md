# range

```python
range(start, end, step)
```

# index

리스트에서 특정 값의 인덱스 찾기

```python
a = [1, 2, 3, 4]
print(a.index(2))
# 1
```

# 거꾸로 iterate

```python
numbers = [1, 2, 3, 4]
length = len(numbers)
for i in range(length):
    print(numbers[length - i])
# 4
# 3
# 2
# 1
```

# 첫 인덱스를 시작으로 거꾸로 iterate

AAA에서 키보드 상하좌우 키로 이름을 정할 때 만약 CAT을 만들고싶을 때
인덱스 0에서 C 만들기
인덱스 2로 가서 T 만들기

```python
numbers = [1, 2, 3, 4]
length = len(numbers)
for i in range(length):
    print(numbers[-i])
# 1
# 4
# 3
# 2
```

# [:n]

n번째까지

# [n:]

n번째부터

[['', '', '', '', ''], ['group', 'group', 'group', 'group', 'group'], ['rice', 'rice', 'rice', 'rice', 'rice']
, ['instant', 'instant', 'instant', 'instant', 'instant'], ['noodle', 'noodle', 'noodle', 'noodle', 'noodle']]


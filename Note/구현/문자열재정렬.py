# str = input()
from curses.ascii import isalpha

string = 'K1KA5CB7'
result = []
sum = 0

for i in string:
  if i.isalpha():
    result.append(i)
  else:
    sum += int(i)

result.sort()
if sum != 0:
  result.append(str(sum))

print(''.join(result))


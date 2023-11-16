import re
strings = input()
d = re.findall(r'-?\d+', strings)
sum = sum(map(int, d))
print(sum)

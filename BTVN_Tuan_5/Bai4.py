n = int(input())
a = input().split()
b = tuple(a)
print(b)

count = 0
for i in range(len(b)):
    if b[i].isdigit():
        count += 1
print(count)
n = int(input())
m = map(int, input().split())
x = int(input())
sum = 0
a = set()
for i in m:
    sum += i
    if (sum > x):
        break
    a.add(i)

print(a)
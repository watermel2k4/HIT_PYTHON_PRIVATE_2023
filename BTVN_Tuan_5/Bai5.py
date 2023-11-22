n = set(map(int, input().split()))
m = tuple(n)
print(n if 11 in n else n | {11})

b = []
for i in range(len(n) - 1):
    for j in range(i + 1,len(n)):
        if (m[i] + m[j] == 11):
            b.append((m[i],m[j]))
print(tuple(b))

print(sum(a for i in tuple(b) for a in i))
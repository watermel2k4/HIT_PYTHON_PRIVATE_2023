n = list(map(int, input().split()))
m = sorted(n)
result = []
l = []
for i in m:
    if not l or i == l[-1]:
        l.append(i)
    else:
        result.append(l)
        l = [i]
if l:
    result.append(l)
print(result)

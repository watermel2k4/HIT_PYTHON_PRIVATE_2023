n = input().split()
l = []
for i in n:
    find = False
    for a in l:
        if a[0] == i:
            a[1] += 1
            find = True
            break
    if not find:
        l.append([i,1])
            
print(tuple(tuple(i) for i in l))
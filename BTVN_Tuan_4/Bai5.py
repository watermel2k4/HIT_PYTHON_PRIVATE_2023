list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l = []
for item in list:
    if isinstance(item, int):
        l.append(item)
    else:
        for num in item:
            l.append(num)
print(l)
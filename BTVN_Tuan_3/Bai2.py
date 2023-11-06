n = int(input("Nhập n (5 <= n <=100): "))
m = int(input("Nhập m (m >= 3): "))
y = []
for i in range(n):
    x = input()
    y.append(x [:m] + x[:-m-1:-1])
print(y)


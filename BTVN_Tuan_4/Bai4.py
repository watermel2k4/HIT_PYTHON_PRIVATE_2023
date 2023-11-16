n = input()
m = list(map(int, input().split()))
result = "enven" if sum(i for i in m if int(i) % 2 == 0) > sum(i for i in m if int(i) % 2 != 0) else "odd"
print(result)

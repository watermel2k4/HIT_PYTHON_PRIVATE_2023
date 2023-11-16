import random
m = list(map(str, input().split()))
n = int(input())
random.shuffle(m)
result = [m[i::n] for i in range(n)]
print(result)
n = int(input())
m = list(map(float, input().split()))
def total(m,x):
    sum = 0
    for i in range(x + 1):
        sum += m[i]
    return sum
t = int(input())
for i in range(t):
    x = int(input())
    print(total(m,x))
n = int(input())
A = []
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)   
def faction(A):
    element  = 1
    sample  = 1
    """
        tính tổng tử số và mẫu số
    """
    for i in A:
        element *= i[0]
        sample *= i[1]
    return element,sample
def UCLN(a,b):
    """
        Tính UCLN giữa tử và mẫu
    """
    if (b == 0):
        return a
    return UCLN(b,a % b) 
element,sample = faction(A)
print((element // UCLN(element,sample)),(sample // UCLN(element,sample)))

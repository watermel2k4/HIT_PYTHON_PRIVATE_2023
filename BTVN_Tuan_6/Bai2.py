n,m = int(input("Nhập dòng: ")), int(input("Nhập cột: "))
Matrix = []
for i in range(n):
    B = []
    for j in range(m):
        a = int(input("Nhập phàn tử thứ [{}][{}]: ".format(i,j)))
        B.append(a)
    Matrix.append(B)
def move(Matrix):
    """
        đảo vị trí ma trận
    """
    Matrix_T = [[Matrix[j][i] for j in range(n)] for i in range(m)]
    for item in Matrix_T:
        print(*item)

move(Matrix)
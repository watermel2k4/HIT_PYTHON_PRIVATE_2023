class Matrix():
    def __init__(self,hang, cot, values):
        self.hang = hang
        self.cot = cot
        self.values = values
    def __add__(self, other):
        if self.hang != other.hang or self.cot != other.cot:
            return False
        result_add = [[self.values[i][j] + other.values[i][i] for j in range(self.cot)] for i in range(self.hang)]
        return Matrix(self.hang,self.cot,result_add)
    def __sub__(self, other):
        if self.hang != other.hang or self.cot != other.cot:
            return False
        result_sub = [[self.values[i][j] - other.values[i][i] for j in range(self.cot)] for i in range(self.hang)]
        return Matrix(self.hang,self.cot,result_sub)
    def __mul__(self, other):
        if self.cot != other.hang:
            return False
        result_mul = [[sum(self.values[i][k] * other.values[k][j] for k in range(self.cot)) for j in range(other.cot)] for i in range(self.hang)]
        return Matrix(self.hang,self.cot,result_mul)

    def __eq__(self, other):
        if self.hang != other.hang or self.cot != other.cot:
            return False
        return all([self.values[i][j] == other.values[i][j] for i in range(self.hang) for j in range(self.cot)])
    def __str__(self):
        return '\n'.join([' '.join(map(str, i)) for i in self.values])

matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
matrix2 = Matrix(2, 2, [[5, 6], [7, 8]])

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

print("Cộng 2 ma trận:")
print(matrix1 + matrix2)

print("Trừ 2 ma trận:")
print(matrix1 - matrix2)

print("Nhân 2 ma trận:")
print(matrix1 * matrix2)

print("So sánh 2 ma trận:")
print(matrix1 == matrix2)
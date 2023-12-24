import numpy as np

n = int(input())
a = np.array([int(input(f"Nhập phần tử a[{i}]: ")) for i in range(n)])
b = np.array([int(input(f"Nhập phần tử b[{i}]: ")) for i in range(n)])

print("Vector a:")
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Giá trị trung bình:", np.mean(a))
print("Độ lệch chuẩn:", np.std(a))
print("Giá trị trung vị:", np.median(a))

print("Vector b:")
print("Max:", np.max(b))
print("Min:", np.min(b))
print("Giá trị trung bình:", np.mean(b))
print("Độ lệch chuẩn:", np.std(b))
print("Giá trị trung vị:", np.median(b))

c = np.vstack((a, b)).T
print("Ma trận c:")
print(c)

mean_b = np.mean(b)
std_b = np.std(b)
d = np.random.normal(loc=mean_b, scale=std_b, size=(n, n))
print("Ma trận d:")
print(d)

sum_result = c + d
signal_result = c - d
accumulation_result = np.dot(c, d)
inverse_d = np.linalg.inv(d)
accumulation_inverse = np.dot(d.T, inverse_d)

print("Tổng của c và d:")
print(sum_result)
print("Hiệu của c và d:")
print(signal_result)
print("Tích của c và d:")
print(accumulation_result)
print("Tích của ma trận chuyển vị của d và ma trận nghịch đảo của d:")
print(accumulation_inverse)


e = np.expand_dims(c, axis=0)
print("Tensor e:")
print(e)

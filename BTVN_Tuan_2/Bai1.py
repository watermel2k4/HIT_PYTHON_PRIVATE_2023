a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

print("Kết quả a cộng b là:", a + b)

print("Kết quả a trừ b là:", a - b)

print("Kết quả a nhân b là:", a * b)

print("Kết quả a chia lấy nguyên b là:", a // b)

print("Kết quả a mũ b là:", a ** b)

print("Kết quả a chia dư b là:", a % b)

print("Kết quả a lớn hơn b là:", a > b)

print("Kết quả a nhỏ hơn b là:", a < b)

print("Kết quả a bằng b là:", a == b)

print("Kết quả a AND b là:", a & b)

print("Kết quả a OR b là:", a | b)

print("Kết quả a XOR b là:", a ^ b)

print("Kết quả NOT a == b là:", ~(a == b))

print("Kết quả a dịch phải 5 bit là:", a >> 5)

print("Kết quả a dịch trái 6 bit là:", a << 6)

while a < 0:
    a = int(input("Nhập lại số a: "))
b = a
result = ""
while a > 0:
    result = str(a % 2) + result
    a = a // 2
print("Hệ số 2 cơ số đảo ngược của {} là:".format(b), result[::-1])
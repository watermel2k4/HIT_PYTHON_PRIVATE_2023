a = int(input("Nhập a: "))

print("Số lượng bit cần thiết không bao gồm phần dấu và các số 0 ở đầu của {} là:".format(a), a.bit_length())

print(dir(a))
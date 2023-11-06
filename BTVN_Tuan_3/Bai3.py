k = int(input("NhậP số học sinh: "))
for i in range(k):
    name= input()
    t1 = int(input())
    t2 = int(input())
    result = "Xuất sắc" if t1 + t2 >= 190 else "Giỏi" if t1 + t2 >= 150 else "Khá" if t1 + t2 >= 100 else "Yếu"
    print(i + 1, name, t1 + t2, result)
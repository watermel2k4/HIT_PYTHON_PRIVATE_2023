n,m = int(input()),int(input())
ban1,ban2 = set(),set()

for i in range(n):
    a = input("Nhap thong tin sinh vien thu {}: ".format(i + 1))
    ban1.add(a)

for i in range(m):
    b = input("Nhap thong tin sinh vien thu {}: ".format(i + 1))
    ban2.add(b)
if (ban1 & ban2) == "":
    print("khong co SV nao dangh ki 2 ban")
else:
    print("Danh sach SV dang ki o 2 ban:", ban1 & ban2)

print("Danh sach SV dang ki 2 ban:", ban1 | ban2)

print("Danh sach SV dang ki ban 1 khong dang ki ban 2:", ban1 - ban2)

print("Danh sachg SV dang ki 1 ban duy nhat:", ban1 ^ ban2)
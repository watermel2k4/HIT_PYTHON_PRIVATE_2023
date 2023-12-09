class Hiter():
    danh_Sach_hiter = []
    def __init__(self,id, name, age, gener):
        self.id = id
        self.name = name
        self.age = age
        self.gener = gener
        Hiter.danh_Sach_hiter.append(self)
    @classmethod
    def nhap(cls):
        id = input("Nhập ID: ")
        name = input("Nhập Tên: ")
        age = input("Nhập Tuổi: ")
        gener = input("Nhập Thế hệ: ")
        return cls(id, name, age, gener)
     
    @staticmethod
    def danhSach():
        print("Danh sách tất cả Hiter:")
        for hiter in Hiter.danh_Sach_hiter:
            print(hiter)
    def __str__(self):
        return f"ID: {self.id} - Tên: {self.name} - Tuổi: {self.age} - Thế hệ: {self.gener}"  
    
class Ban():
    danh_Sach_Ban = []
    def __init__(self, idBan,  tenBan, hiter_truongban, thanhvien):
        self.idBan = idBan
        self.tenBan = tenBan
        self.hiter_truongban = hiter_truongban
        self.thanhvien = thanhvien
    @classmethod
    def nhap(cls, m):
        for i in range(m):
            idBan = input("Nhập ID Ban: ")
            tenBan = input("Nhập Tên Ban: ")
            hiter_truongban = Hiter.nhap()
            thanhvien = []
            for j in range(int(input("Nhập số thành viên trong ban: "))):
                thanh_vien = Hiter.nhap()
                thanhvien.append(thanh_vien)
            ban = cls(idBan, tenBan, hiter_truongban, thanhvien)
            cls.danh_Sach_Ban.append(ban)
    def __str__(self):
        return f"ID Ban: {self.idBan}, Tên Ban: {self.tenBan}, Hiter trưởng ban: {self.hiter_truongban}, thành Viên: {self.thanhvien}"
    @staticmethod
    def danhSachBan():
        for ban in Ban.danh_Sach_Ban:
            print(f"ID Ban: {ban.idBan}, Tên Ban: {ban.tenBan}")
            print(f"Hiter trưởng: {ban.hiter_truongban}")
            print("Danh sách thành viên:")
            for thanh_vien in ban.thanhvien:
                print(thanh_vien)
    @classmethod
    def xoa(cls, ten_Ban, id_hiter):
        for ban in cls.danh_Sach_Ban:
            if ban.tenBan == ten_Ban:
                for hiter in ban.thanhvien:
                    if hiter.id == id_hiter:
                        ban.thanhvien.remove(hiter)
                        cls.danhSachBan()
                        print(f"Đã xóa Hiter với ID {id} khỏi Ban {ten_Ban}")
                        return
                    print(f"Không tìm thấy Hiter với ID {id} trong Ban {ten_Ban}")
                    return
                print(f"Không tìm thấy Ban có tên {ten_Ban}")
                    

    @classmethod
    def them(cls, ten_Ban, id):
        for ban in cls.danh_Sach_Ban:
            if ban.tenBan == ten_Ban:
                hiter_exists = None
                for hiter in Hiter.danh_Sach_hiter:
                    if hiter.id == id:
                        hiter_exists = hiter
                        break
                if hiter_exists not in [member for member in ban.thanhvien]:
                    ban.thanhvien.append(hiter_exists)
                    cls.danhSachBan()
                    print(f"Đã thêm Hiter với ID {id} vào Ban {ten_Ban}")
                    return
                elif not hiter_exists:
                    print(f"Không tìm thấy Hiter với ID {id}")
                    return
                else:
                    print(f"Hiter với ID {id} đã tồn tại trong Ban {ten_Ban}")
                    return
        print(f"Không tìm thấy Ban có tên {ten_Ban}")



n = int(input("Nhập số lượng Hiter: "))
for _ in range(n):
    Hiter.nhap()
Hiter.danhSach()

m = int(input("Nhập số lượng Ban: "))
Ban.nhap(m)
Ban.danhSachBan()

ten_ban_can_xoa = input("Nhập tên Ban cần xóa Hiter: ")
id_hiter_can_xoa = input("Nhập ID Hiter cần xóa: ")
Ban.xoa(ten_ban_can_xoa, id_hiter_can_xoa)

ten_ban_can_them = input("Nhập tên Ban cần thêm Hiter: ")
id_hiter_can_them = input("Nhập ID Hiter cần thêm: ")
Ban.them(ten_ban_can_them, id_hiter_can_them)
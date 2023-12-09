from math import gcd #(hàm tìm UCLN)

class PhanSo():
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.rut_gon()
    def rut_gon(self):
        ucln = gcd(self.tu_so,self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
    @staticmethod
    def honSoToPhanSo(hon_so):
        phan_nguyen = hon_so.phan_nguyen
        tu_so = hon_so.phan_so.tu_so
        mau_so = hon_so.phan_so.mau_so
        return PhanSo(phan_nguyen * mau_so + tu_so, mau_so)


class HonSo():
    def __init__(self, phan_nguyen, phan_so):
        self.phan_nguyen = phan_nguyen
        self.phan_so = phan_so

    @staticmethod
    def phanSoToHonSo(phanso):
        phan_nguyen = phanso.tu_so // phanso.mau_so
        phan_so_tu = phanso.tu_so % phanso.mau_so
        return HonSo(phan_nguyen, PhanSo(phan_so_tu, phanso.mau_so))

class Math():
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return Math(self.a + other.a)

    def __mul__(self, other):
        return Math(self.a * other.a)

    def __str__(self):
        return str(self.a)

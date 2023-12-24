import numpy as np

diem = np.random.randint(0, 11, size=(3, 20))

print("Điểm lớn nhất mỗi môn:")
print(np.max(diem, axis=1))

print("Điểm nhỏ nhất mỗi môn:")
print(np.min(diem, axis=1))

diem_phang = diem.flatten()
diem_phang = diem_phang[diem_phang != 0]
print("Mảng sau khi làm phẳng và loại bỏ điểm 0:")
print(diem_phang)

diem_sapxep = np.sort(diem_phang)[::-1]
print("Mảng sau khi sắp xếp giảm dần:")
print(diem_sapxep)

k = float(input("Nhập số thực k: "))

vi_tri_chen = np.searchsorted(diem_sapxep, k, side='right')
print(f"Vị trí chèn {k} vào mảng mà không phá vỡ tính sắp xếp: {vi_tri_chen}")

diem_sapxep = np.insert(diem_sapxep, vi_tri_chen, k)
print("Mảng sau khi thêm giá trị k:")
print(diem_sapxep)

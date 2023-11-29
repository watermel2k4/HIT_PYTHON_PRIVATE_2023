import math
def read(file):
    """
        dùng with để đọc file và thực thi câu lệnh 
        thoát khỏi with thì nó sẽ tự đọng close file
        muốn truy cập lại thì phải gọi lại
        with open("tên file", mode = '') as "tên đặt"
    """
    with open(file) as fobj:
        data = fobj.read().split()
    coordinates = {}
    value = ''
    for i in data:
        if i.isalpha():
            value = i
            coordinates[value] = []
        else:
            coordinates[value].append(float(i))
    return coordinates

def distance(x,y):
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)

def write(file,coordinates):
    """
        đọc file và ghi lại dùng 'w' mở để ghi trước đó sẽ xoá hết ND hiện có
        có thể dùng a+ thay w để ghi tiếp k xoá ND hiện có
    """
    with open(file, 'w') as fobj:
        fobj.write(f"A({coordinates['A'][0]},{coordinates['A'][1]})")
        fobj.write(f"B({coordinates['B'][0]},{coordinates['B'][1]})")
        result = distance(coordinates['A'],coordinates['B'])
        fobj.write(f"AB = {result:.2f}")

read_file = read('E:\\python\\private\\Tuan_6\\input.txt')
write('E:\\python\\private\\Tuan_6\\output.txt', read_file)
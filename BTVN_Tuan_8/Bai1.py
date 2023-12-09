class Pycon():
    automatic_id = 0
    total_age = 0
    total_pycons = 0
    def __init__(self,name,age):
        Pycon.automatic_id += 1
        self.id = Pycon.automatic_id
        self.name = name
        self.age = age
        Pycon.total_age += age
        Pycon.total_pycons += 1 
    def avg_age(self):
        if self.total_pycons == 0:
            return 0
        return self.total_age / self.total_pycons
    def display(self):
        print(f"ID: {self.id} || Tên: {self.name} || Tuổi: {self.age}")

n = int(input())
pycons = []
for i in range(n):
    name = input().strip()
    age = int(input().strip())
    pycon = Pycon(name,age)
    pycons.append(pycon)

for a in pycons:
    a.display()
Avg = pycon.avg_age()
print(f"Trung bình tuổi: {Avg}")
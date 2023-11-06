import math
print("Nhập toạ độ A:")
xA= int(input())
yA= int(input())
print("Nhập toạ độ B:")
xB= int(input())
yB= int(input())
print("Nhập toạ độ C:")
xC= int(input())
yC= int(input())
def triangular(xA,yA,xB,yB,xC,yC):
    AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
    BC = math.sqrt((xC - xB)**2 + (yC - yB)**2)
    CA = math.sqrt((xA - xC)**2 + (yA - yC)**2)
    if (AB + BC > CA and AB + CA > BC and CA + BC > AB):
        print("TAM GIÁC")
    else:
        print("KHÔNG PHẢI TAM GIÁC")
print(triangular(xA,yA,xB,yB,xC,yC))
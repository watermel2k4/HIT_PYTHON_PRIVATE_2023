championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Tryndamere"]

dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}	
]

dic = {}

for i in range(len(championLOL)):
    key = championLOL[i]
    value = dataLOL[i]
    dic[key] = value
for i in dic:
    print(i,end=": ")
    print(dic[i])

s = input()
if s in dic:
    print(dic[s]["price"])
SV = {'SV001' : 0.9,
       'SV002' : 2.8,
       'Sv003' : 3.3,
       'SV004' : 8,
       'SV005' : 3.6}
count = 0
for x in SV:
    if SV[x] >= 2.5 and SV[x] <= 3.5:
        count += 1
print(count)

SV["SV006"] = 3.0

for x in list(SV):
    if SV[x] < 2:
        del SV[x]

print(SV)


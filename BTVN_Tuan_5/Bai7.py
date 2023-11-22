n = input()
dic ={}
for i in n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
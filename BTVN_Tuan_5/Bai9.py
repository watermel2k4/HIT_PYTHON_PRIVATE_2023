import random
n = int(input("n (10 < n < 100000): "))
lst = ["CNTT", "KHMT", "KTPM", "HTTT"]
Account = {}
for i in range(n):
    msv = "20216{:05d}".format(i + 1)
    mk = random.choice(lst) + msv
    info = {
        "Username" : msv,
        "Password" : mk
    }
    Account["Account{}".format(i + 1)] = info

for i in Account:
    print(i,end=": ")
    print(Account[i])

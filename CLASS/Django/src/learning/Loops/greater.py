import random as r
num=int(input("enter num"))
while True:
    a=r.randrange(100)
    print(a)
    if num<a:
        break
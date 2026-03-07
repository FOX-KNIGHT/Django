import re as r
def email(input):
    input=input("sid@gmail.com")
    p=r"([a-zA-Z]*@[a-z]{4-6}.[a-z]{2-4})"
    valid=r.match(p,input)
    print(r.match(p,input))



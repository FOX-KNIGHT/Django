s="a4b6c3"
s1=""
for i in s:
    if i.isalpha():
        temp=i
    else:
        s1=int(i)+ord(temp)
        print(temp+chr(s1),end="")
a=[]


a.append(1)

a.append(10)
a.append(10)
a.append(14)
a.append(145)

a.append("100")
a.append("abc")
a.append(105)
a.append(a[3])


s=set(a)
print(type(s))
print(s)
s.add(10)
s.add(13)
print(s)
for i in s:
    print(i)

x=10,20,30
print(type(x))
print(x)
x1=(2,)
print(type(x1))
print(x1)

x2=tuple(a)
print(type(x2))
print(x2)
print(x2[3])



t,y,u=x
print(x)
[]
a=[]
print(type(a))
print(a)
print(id(a))
a.append(1)
print(a)
print(id(a))
a.append(10)
a.append(10)
a.append(14)
a.append(145)
print(a)
print(a[4])
a.append("100")
a.append("abc")
a.append(105)
print(a)
print(a[3])
a.append(a[3])
print(a)

for i in a[::-2]:
    print(i, end=",")
print( )
for i in range(-1,-len(a)-1,-1):
    print(a[i], end=",")

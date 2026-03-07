l=[0,1,2,3,4,5,6,7,8]
print(l[0])
print(l[1:3])
print(l[-4:-1])

l2=l[1:3]
l2[1]=14
print(l2)
print(id(l))
print(id(l2))

l3=l
print(id(l3))
l3[2]=20
print(l)
print(l2)
print(l3)

l4=l[:]
print(id(l4))
l4[4]=400
print(l)
print(l4)
print()

l5=l.copy()
l5[6]=600
print(l)
print(l5)

print("1:",id(l))
print("2:",id(l2))
print("3:",id(l3))
print("4:",id(l4))
print("5:",id(l5))

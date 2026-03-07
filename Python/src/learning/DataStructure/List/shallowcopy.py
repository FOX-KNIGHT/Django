import copy

l1=[0,1,2,[3,4],5]
l2=l1[:]
l3=l1.copy()
l4=copy.deepcopy(l1)

print(l1[3][0])
l1[3][1]=5
l1[3][0]=30
l1[0]=100
l1[0]=4
print("1:",l1,id(l1))
print("2:",l2,id(l2))
print("3:",l3,id(l3))
print("4:",l4,id(l4))

print(id(l1[0]))
print(id(l2[0]))
print(id(l3[0]))
print(l1[3],id(l1[3]))
print(l2[3],id(l2[3]))
print(l3[3],id(l3[3]))

print()
print(l1[0],id(l1[0]))
print(l1[3][1],id(l1[3][1]))



a=5
b=5
print(a is b)
print(a==b)
print()

l1=['abc','def']
l2=['abc','def']
print(id(l1),id(l2))
print("l1 is l2:",l1 is l2)
print("l1==l2:",l1==l2)
l3=l1
print()
print(id(l1))
print("l1 is l2:",l1 is l2)
print("l1==l2:",l1==l2)
print("l1 is l3:",l1 is l3)
print("l2 is l3:",l2 is l3)
print("l1==l3:",l1==l3)
print("l2==l3:",l2==l3)
print()

print("---- After----")


l1.append("sid")
print("l1:",l1)
print("id l1:",id(l1))
print("id l2:",id(l2))
print("id l3:",id(l3))

print()
print("l1 is l2:",l1 is l2)
print("l1==l2:",l1==l2)
print("l1 is l3:",l1 is l3)
print("l2 is l3:",l2 is l3)
print("l1==l3:",l1==l3)
print("l2==l3:",l2==l3)
print()

x=10.0
y=10.0
print(x==y)
print(x is y)
l1=[1,2,3,4,"5",1,2]
l1.append(-5)
print(l1)
l1.clear()
print(l1)
"""del l1"""
print(l1)

l2=[1,4653,5436,34,2,1,3,4,24,2]
l1.append("iter")
l1.extend("iter")
l1.extend(l2)
l1.insert(2,"SOA")
print(l1)
print()

l1.remove("iter")
print(l1)
print()

print(l2.count(1))
print(l2.index(2))
print()

print(l1.pop())
print(l1)
print(l1.pop(3))
print(l1)
print()

l3=[11,2,9,3,5]
l3.sort(reverse=True)
print(l3)
print()

l3.reverse()
print(l3)
print()
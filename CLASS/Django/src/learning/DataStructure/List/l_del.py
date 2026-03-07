l1=["Kuch",7,18,19,24]
l1.append(77)
print(l1)
l1.insert(2,1)
print(l1)

l1.insert(0,12)
print(l1)

l1.remove(1)
print(l1)
print(id(l1))
l1*=2 #wont be same in l1=l1*2
print(l1)
print(id(l1))
print()

l1.extend(l1)
print(l1)

l1.remove(24)
print(l1)

l1.clear()
print(l1)
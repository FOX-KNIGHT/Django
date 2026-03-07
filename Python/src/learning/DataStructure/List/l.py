l1=[0,1,2,3,4,5,6]
l1[1:5]=[2,3,4,5]
print(l1)
print()
l1[1:3]=[3,3,3,3,3]
print(l1)
print()

l1[:]=[3]
print(l1)
print()

l2=[0,4,5,6]
"""l2[1:1]=[1,2,3]
print(l2)
l2[:0]=[1]
print(l2)

l2[3:3]=(8,9,11)
print(l2)
print()"""

l1[1:1]=l2
print(l1)
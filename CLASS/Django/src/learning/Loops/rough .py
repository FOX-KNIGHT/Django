a=range(10)
print(id(a))
print(type(a))

b=range(10)
print(id(b))
print(a)
print()



b=[0,1,2,3,4,5,6,7,8,9]
b[0:10]
for i in b[7:-1:-1]:
    print(i)
    
print()

a="abc" in 'abcd'
print(a,type(a))

if "a" in "abc":
    print("yes")

a=5;b=5
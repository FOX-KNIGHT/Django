a={1,2,3}
print(a)
a.add("iter")
print(a)

l1=["a","b","c"]
a.update(l1)
print(a)

a.update("iter")
print(a)


l2=["x","y","z"]
a.update(l2,"Soa")
print(a)

for i in a:
    print(i)
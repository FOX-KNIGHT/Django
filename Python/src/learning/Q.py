s="abc   def efg"
print(s.split())
print("".join(s.split()))

l=[" abc", " def ","efg "]
print("".join(l))
for i in l:
    print("The id of", id(i))

for i in range(0,len(l)):
    l[i].strip()

print(l)
for i in l:
    print("The id of", id(i))


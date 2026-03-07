l1=[1,"a","bc",123]
print(list(enumerate(l1,1)))

for i,j in enumerate(l1):
    print(i,". ",j,sep="")

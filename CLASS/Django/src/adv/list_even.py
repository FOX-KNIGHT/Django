l1=[]
n=20
for i in range(0,n+1):
    if i%2==0:
        l1.append(i)
print(l1)

l2=[i for i in range(1,n+1) if i%2==0]
print(l2)
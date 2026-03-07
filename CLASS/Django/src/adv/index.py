l1=[1,3,111,4,2,3,22,99,3,66,0]
ind=0
max=0
for i in range(len(l1)-1):
    if max<l1[i]:
        max=l1[i]
        ind=i

print(ind)
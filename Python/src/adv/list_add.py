l1=[1,9,9]
for i in range(len(l1),0,-1):
    if l1[i-1]==9:
        l1[i-1]=0
    else:
        l1[i-1]+=1
        break

else:
    l1.insert(0,1)

print(l1)
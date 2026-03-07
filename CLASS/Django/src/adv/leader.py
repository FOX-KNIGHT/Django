l1=[1,2,10,8,6,7,-1]
max=l1[-1]
for i in range(len(l1)-1,-1,-1):
    if l1[i]>=max:
        max=l1[i]
        print(max)

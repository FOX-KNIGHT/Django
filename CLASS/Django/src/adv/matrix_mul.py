l1=[[1,2],[5,4]]
l2=[[3,4],[5,6]]
l3=[[0,0],[0,0]]

for i in range(0,len(l1)):
    for j in range(0,len(l1)):
        for k in range(0,len(l1)):
            l3[i][j]+=l1[i][k]*l2[k][j]

for i in l3:
    print(i)
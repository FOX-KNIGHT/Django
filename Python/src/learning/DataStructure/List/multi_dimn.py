big_list=[1]*100
print(big_list)
mat=[[0]*20]*20

mat1=[]
for i in range(20):
    mat1.append([19]*i)

for i in mat1:
    print(i)

print()
mat2 = [[7]*10 for _ in range(20)]
for i in mat2:
    print(i)


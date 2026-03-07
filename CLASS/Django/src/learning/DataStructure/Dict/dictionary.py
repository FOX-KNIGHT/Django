d1={"Siddhant":18,"Mithilesh":19,"Sujal":20,"Rohit":23}
print(d1)
for i in d1:
    print(i,d1[i],sep=" ->age-")

print()

d1["Rohit"]=21
for i in d1:
    print(i,d1[i],sep=" ->age-")
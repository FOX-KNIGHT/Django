s="I am Siddhant aka fox_Knight"
v="AEIOUaeiou"
count=0
res=[]
for i in s:
    if i in v:
        res.append(i)
        count+=1
print(res)
print('Total Vowel:',count)

vc={"A":0,"E":0,"I":0,"O":0,"U":0}
for i in s:
    if i.upper() in vc:
        vc[i.upper()]+=1
print(vc)
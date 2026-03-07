import functools as f

def func_endswith(a):
    if a.endswith(".com") and "@" in a:
        return a
    else:
        return ""

s=["mith@gmail.com","sidgmail.com","mithelesh@yahoo.com","sid@gmail.com","sidd@yahoo.org","siddhant@gmail.com"]

#print(list(filter(func_endswith,s)))
#print(list(filter(lambda x:"@"in x and x.endswith(".com"),s)))
"""d1={}
for i in domain:
    d1[i]=domain.count(i)
print(d1)
cg=0
yg=0
for i in range(len(s)-1):
    if domain[i][0]=="g":
        cg+=1
    else:
        yg+=1
print("Google", cg, "Yahoo:",yg)"""


res = list(filter(lambda x:(x.endswith(".com") or x.endswith(".org")) and "@" in x,s))
domain=[s.split("@")[1].split(".")[0] for s in res]
print(domain)
count={i:domain.count(i) for i in domain}
print(count)



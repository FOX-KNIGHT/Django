import functools
n=5
l1=list(range(1,n+1))
print(l1)

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

pdt=1
sum=0
for i in range(1,n+1):
    a = sum
    b = i
    sum = add(a,b)

    a1=pdt
    b1=i
    pdt=mul(a1,b1)
print("Sum:",sum)
print("Product:",pdt)

result=functools.reduce(add,l1)
fact=functools.reduce(mul,l1)
print(result)
print(fact)
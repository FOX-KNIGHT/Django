import functools as ft

lam1=lambda a,b: a+b
n=5
l1=list(range(1,n+1))
print(ft.reduce(lam1,l1))


sum=lam1(2,3)
print(sum)
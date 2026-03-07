"""a=int(input("Enter number:"))
b=int(input("Enter number:"))
r=b%a
while r!=0:
    b=a
    a=r
    r=b%a
print(a)
"""
a=int(input("Enter number:"))
b=int(input("Enter number:"))
r=min(a,b)
while a%r!=0 or b%r!=0:
    r-=1
print(r)
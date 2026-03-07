a=int(input("Enter first Side:"))
b=int(input("Enter second Side:"))
c=int(input("Enter third Side:"))


def area(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**.5

print("Area of triangle with sides {} ,{} and {} is {}:" .format(a,b,c,area(a,b,c)))
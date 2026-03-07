def max(a,b,c):
    if a>b and a>c:
        return print("First number is greater", end=" ")
    elif c>b and c>a:
        return print("Third number is greater", end=" ")
    else:
        return print("Second number is greater", end=" ")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
print("Among the number ".format(max(a,b,c)))
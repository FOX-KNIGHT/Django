a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

print("Max:",a if (a>b and a>c) else c if (c>a and c>b) else b if (b>a and b>c) else "all are equal")

s1="hello"
print(s1[-3:0:-1])
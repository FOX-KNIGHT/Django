stack=[]
res=[]
eq=input("Enter the Equation:")
eq=eq.split()

for i in eq:
    if i.isdigit():
        res.append(i)
    else:
        stack.append(i)
        if stack.append(i)==['+' or '-'] and stack.append(i-1)==['/' or '*']:
            res.append(stack.pop())
            stack.append(i)
        elif i==len(eq):
            res.append(stack.pop())
        else:
            stack.append(i)

print("Result:",res)
print("Result:",stack)
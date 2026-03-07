z=input("Enter the elements for stack:")

stack=[]
z=z.split()

for i in z:
    if i not in ['+','-','*','/']:stack.append(i)
    else:
        x=stack.pop()
        y=stack.pop()
        """stack.append(str(eval(x+i+y)))"""
        
        
        """if i== "+":
            z=x+y
        elif i=="-":
            z=x-y
        elif i=="*":
            z=x*y
        else:
            z=x/y
            if y== 0:
                
        stack.append(z)"""
        
print("Result:",stack.pop())
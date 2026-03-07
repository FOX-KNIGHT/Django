def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

ch=int(input("hi"))
fn=[add,sub,mul]
fn_call=fn[ch-1]
print(fn_call(5,3))


"""dn={"add":addition,"sub":subtraction,"mul":multiplication}
inp=input("Enter any operation:")

dn_call=dn[inp]
print(dn_call(5,3))
"""

add(a=4,b=5)
def ret(x):
    return x[1]

data=[(-4,5),(1,0),("hello",2),(3.5,1)]
data1=[(-4,5),(1,0),(5,2),(3,1)]
data2=["siddhant","sujal","mithilesh","rohit","iit"]

"""print(sorted(data, key=ret(x)))""" #gives error
print((sorted(data2)))
print(sorted(data2, key= lambda x:len(x))) #inc the readability of fun

print(sorted(data, key= lambda x: str(x[0]) ))


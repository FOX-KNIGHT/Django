def func(l):
    print(type(l))    
    l[0]=10
    l[1]=2
    l[2]=20
    print(type(l))

s1={5,6,7}
l1=[1,2,3]
l1[0]=20

func(l1)
print(l1)

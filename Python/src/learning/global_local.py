count=10
print(id(count))

def fun_a():
    global count
    count=20
    print(count)
    print(id(count))

def fun_b():
    print(count)
    print(id(count))

def fun_c():
    count=20
    print(count)
    print(id(count))


fun_a()
fun_b()
fun_c()
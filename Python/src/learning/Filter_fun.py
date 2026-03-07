def func_endswith(a):
    if a.endswith(".com"):
        return a
    else:
        return None

l1=["a.com","b.com","c.com","d","s.com"]
print(list(filter(func_endswith,l1)))

lam1=filter(lambda x:x.endswith(".com"),l1)
print(list(lam1))

func_endswith()

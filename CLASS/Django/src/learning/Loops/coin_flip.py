import random as r
prev=-1
while True:
    a=r.randrange(0,2)
    res='Heads' if a==0 else 'Tails'
    if res=='Heads':
        current=0
    else:
        current=1
    print(res,"it is")
    if prev==current:
        count+=1
    else:
        count=1
        prev=current
    if count==3:
        break
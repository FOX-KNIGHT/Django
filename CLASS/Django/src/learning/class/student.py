from pickle import dump,load
class Student:
    def __init__(self,name,clg_n,redg):
        self.name=name
        self.clg_n=clg_n
        self.redg=redg
    def disp(obj):
        print( obj.name+"\t"+obj.clg_n+"\t"+obj.redg)

inp=int(input("No of records:"))
i=0
data=[]
while i<inp:
    name=input("Enter name:")
    clg_n=input("Enter college name:")
    redg=input("Enter redgistration no:")
    data.append(Student(name,clg_n,redg))
    i+=1

with open("student.txt",'ab+') as f:
    for i in data:
        dump(i,f)
    f.seek(0)
    res=load(f)
    res.display(f)

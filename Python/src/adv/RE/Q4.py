from pickle import dump,load
class Student:
    def __init__(self,name,regd):
        self.name = name
        self.regd = regd
    def __str__(self):
        return "Student Name:{}, Regd No:{}".format(self.name,self.regd)

num = int(input("Enter number of records: "))
lst = []
for i in range(num):
    n = input("Enter Student Name: ")
    reg = input("Enter Regd No.: ")
    lst.append(Student(n,reg))

with open("student.dat","w+b") as f:
    for obj in lst:
        dump(obj, f)
    f.seek(0)
    print("File content:")
    while True:
        try:
            
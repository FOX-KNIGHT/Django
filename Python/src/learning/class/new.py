class stu(int):
    def __new__(cls,a,b):
        if a<20 and b>5:
            return super(stu,cls).__new__(cls)
        else:
            return print("not valid")

    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a,self.b)

stu(3,14)
stu(21,4)
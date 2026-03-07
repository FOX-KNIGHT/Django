Result=[]

def mark_input():
    global Result
    a=input("Enter name of Subject:")
    b=int(input("Enter marks of Student:"))
    return {"Subject": a, "Marks": b}

def stu_input():
    global Result
    name=input("Enter name of Student:")
    marks_list = []
    n = int(input("How many subjects? "))
    for i in range(n):
        marks_list.append(mark_input())
    Result.append({"Name": name, "Marks": marks_list})


def display(a):
    for i in a:
        print(i)

fn=[mark_input,stu_input,display]
print("What do you want to fetch:"
    "\n 1.Student info \n 2.Student marks")
ch=int(input("enter operation:"))
fn_call=fn[ch-1]
print(fn_call())

name = input("\nWhich Student info do you want to fetch? ")
found = False
for student in Result:
    if student["Name"].lower() == name.lower():
        print("\nStudent found:")
        print(student)
        found = True
        break

if not found:
    print("Name not found.")
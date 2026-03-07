stu_info=[]

choice=input("Do you want to enter Syudent Info:")
stu_no=int(input("Enter no of Student:"))
while True:
    if choice in ["Y", "y", "yes", "Yes"]:
        if stu_no!=0:
            stu_name=input("Enter name of Student:")
            stu_marks=int(input("Enter marks of Student:"))
            stu_info.append({"Name": stu_name, "Marks": stu_marks})
            stu_no-=1
        else:
            choice=input("Do you want to enter more Syudent Info:")
            stu_no=int(input("Enter no of Student:"))
    else:
        break

name=input("Which Student info do you want to fetch:")
for i in stu_info:
    if i.get("Name")== name:
        print(i)
    else:
        print("Name not found")
        break

"""
Do you want to enter Syudent Info:y
Enter no of Student:2
Enter name of Student:sidd
Enter marks of Student:90
Enter name of Student:mith
Enter marks of Student:91
Which Student info do you want to fetch:sidd
{'Name': 'sidd', 'Marks': 90"""
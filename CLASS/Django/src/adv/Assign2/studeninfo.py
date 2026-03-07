students=[
    {"info":(101,"sidd"),
    "Marks":[80,85,90],
    "skills":{"c++","python","Java"}},


    {"info":(102,"mith"),
    "Marks":[80,84,91],
    "skills":{"css","html","Java"}}]

def fun(student_profile):

    for stu in student_profile:
        stu_id,stu_name=stu["info"]
        stu_marks=stu["Marks"]
        stu_skills=stu["skills"]

        avg_marks=sum(stu_marks)/len(stu_marks)
        max_marks=max(stu_marks)
        print("ID:",stu_id,"Marks:",stu_marks,"Skills:",stu_skills,"Average Marks:",avg_marks,sep="\n")
        print(max_marks)
fun(students)


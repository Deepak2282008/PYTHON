# Project:Get the student name and marks, find the average and use conditional to give grades.
# print the result for the following marks
# # 90 to 100=A grade
# # 80 to 90=B grade
# # 70 to 80= C grade
# # 60 to 70= D grade
# # below 60= E grade

name=input("Enter your name:")
grade=int(input("Enter your grade:"))
subject=int(input("Enter number of subjects(5 or 6):"))
if grade<=0 or grade>12:
    print("input valid grade")
elif subject==5:
    math=int(input("Enter your math mark:"))
    english=int(input("Enter your english mark:"))
    science=int(input("Enter your science mark:"))
    lang=int(input("Enter your language mark:"))
    social=int(input("Enter your social science mark:"))
    Total=math+english+science+lang+social
    if Total/5>100 or Total/5<0:
        print("Enter valid marks")
    else:
        print("Name:",name)
        print("Grade:",grade)
        print("Total=",Total)
        a=Total/5
        if a>=90 and a<=100:
            print("Grade=A")
        if a>=80 and a<90:
            print("grade=B")
        if a>=70 and a<80:
            print("grade=C")
        if a>=60 and a<70:
         print("grade=D")
        if a<60:
            print("grade=E")


elif subject==6:
    math=int(input("Enter your math mark:"))
    english=int(input("Enter your english mark:"))
    science=int(input("Enter your science mark:"))
    lang=int(input("Enter your language mark:"))
    social=int(input("Enter your social science mark:"))
    AI=int(input("Enter your AI mark:"))
    Total=math+english+science+lang+social+AI
    if Total/6>100 or Total/6<0:
        print("Enter valid marks")
    else:
        print("Name:", name)
        print("Grade:", grade)
        print("Total=",Total)
        a=Total/6
        if a>=90 and a<=100:
         print("Grade=A")
        if a>=80 and a<90:
            print("grade=B")
        if a>=70 and a<80:
            print("grade=C")
        if a>=60 and a<70:
            print("grade=D")
        if a<60:
            print("grade=E")

elif subject<5 or subject>6:
    print("Enter subject 5 or 6")

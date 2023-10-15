def grade(x):
    if(x>=85):
        return 'A+'
    elif(x>=80 and x<85):
        return 'A'
    elif(x>=70 and x<80):
        return 'B+'
    elif(x>=60 and x<70):
        return 'B'
    elif(x>=50 and x<60):
        return 'C+'
    elif(x>=40 and x<50):
        return 'C'
    elif(x>=35 and x<40):
        return 'D'
    else:
        return 'F'

def waitage(x):
    if(x=='A+'):
        return 10
    elif(x=='A'):
        return 9
    elif(x=='B+'):
        return 8
    elif(x=='B'):
        return 7
    elif(x=='C+'):
        return 6
    elif(x=='C'):
        return 5
    elif(x=='D'):
        return 4
    else:
        return 3

def sub_marks():
    midterm=int(input("Enter the marks in mid term out of 25 : "))
    quiz=int(input("Enter the marks in quiz out of 10 : "))
    lab_eval=int(input("Enter the marks in lab evaluation out of 25 : "))
    endterm=int(input("Enter the marks in end term out of 40 : "))
    # final_marks = (midterm/4)+(quiz/10)+(lab_eval/4)+((endterm*2)/5)
    final_marks = midterm+quiz+lab_eval+endterm
    return final_marks

for i in range(5):
    if(i==0):
        print("Input for Maths :\n")
        math_credit = int(input("Enter credits for maths : "))
        math_marks = sub_marks()
        math_grade = grade(math_marks)
        print(f"Grade in mathematics is : {math_grade}\n")
        
    elif(i==1):
        print("Input for Physics : \n")
        phy_credit = int(input("Enter credits for physics : "))
        phy_marks = sub_marks()
        phy_grade = grade(phy_marks)
        print(f"Grade in physics is : {phy_grade}\n")

    elif(i==2):
        print("Input for computing : \n")
        comp_credit = int(input("Enter credits for computing : "))
        comp_marks = sub_marks()
        comp_grade = grade(comp_marks)
        print(f"Grade in computing is : {comp_grade}\n")
    
    elif(i==3):
        print("Input for IEEE : \n")
        ieee_credit = int(input("Enter credits for ieee : "))
        ieee_marks = sub_marks()
        ieee_grade = grade(ieee_marks)
        print(f"Grade in IEEE is : {ieee_grade}\n")
    
    elif(i==4):
        print("Input for communication : \n")
        comm_credit = int(input("Enter credits for communication : "))
        comm_marks = sub_marks()
        comm_grade = grade(comm_marks)
        print(f"Grade in communication is : {comm_grade}\n")

sgpa = ((math_credit*waitage(math_grade))+(phy_credit*waitage(phy_grade))+(comp_credit*waitage(comp_grade))+(ieee_credit*waitage(ieee_grade))+(comm_credit*waitage(comm_grade)))/(math_credit+phy_credit+comp_credit+ieee_credit+comm_credit)

print(f"Your sgpa is : {sgpa}")


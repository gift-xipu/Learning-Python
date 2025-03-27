#activity: inputting students name, marks and adding their details to a dictionary with their name, student number and final marks
#functions include testMark which calculates test mark out of 30%
#assMark which calculates assignment out of 30%
#examMark that calculates a mark out of 40%

finished = "n"
studentRecord = {}
def testAverage(test1, test2, test3):
    average = ((test1 + test2 + test3) / 300 ) * 30
    return average

def assAverage(assignMark):
    average = (assignMark / 100) * 30 
    return average

def examAverage(examMark):
    average = (examMark / 100) * 40 
    return average

def gradeAverage(test, assignment, exam):
    total = test + assignment + exam
    grade = ""
    if total > 50:
        grade = "pass"
    else:
        grade = "fail"
    return grade

while finished == 'n':
    name = input("Enter Student Name: ")
    studentNumber = int(input(f"Enter Student Number for {name}: "))

    #test scores
    test1 = float(input("Enter score for Test 1: "))
    test2 = float(input("Enter score for Test 2: "))
    test3 = float(input("Enter score for Test 3: "))
    test = testAverage(test1, test2, test3)
    
    #assignment scores
    assignMark = float(input("Enter score for the Assignment: "))
    assignment = assAverage(assignMark)

    #exam score
    examMark = float(input("Enter score for the Exam: "))
    exam = examAverage(examMark)

    #record score
    grade = gradeAverage(test, assignment, exam)
    studentRecord[name] = [
        {
        "Student ID:": studentNumber,
         "Grade:": grade,
         }
    ]

    finished = input(("Student Recorded, would you like to add more? (y/n): "))

print(studentRecord)




    
    



    


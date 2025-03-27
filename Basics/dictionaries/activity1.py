finished = "y"
studentRecord = {}

def searchStudent(name):
    if name in studentRecord:
        return studentRecord[name]
    else:
        return "Student not found"

def deleteStudent(name):
    if name in studentRecord:
        del studentRecord[name]
        return f"{name} has been deleted"
    else:
        return "Student not found"

def testAverage(test1, test2, test3):
    average = ((test1 + test2 + test3) / 300) * 30
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

while finished.lower() == 'y':
    if len(studentRecord) != 0:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        search = input("What would you like to do?\n1: Search student\n2: Delete a student\n3: Add a new student\nEnter choice (1-3): ")
        
        if search == "1":
            option = input("Enter name of the student to search: ")
            result = searchStudent(option)
            print(result)
            finished = input("Would you like to continue? (y/n): ")
            continue
            
        elif search == "2":
            option = input("Enter name of the student to delete: ")
            result = deleteStudent(option)
            print(result)
            finished = input("Would you like to continue? (y/n): ")
            continue
    
    # Add new student
    name = input("\nEnter Student Name: ")
    studentNumber = int(input(f"Enter Student Number for {name}: "))
    
    # Test scores
    test1 = float(input("Enter score for Test 1: "))
    test2 = float(input("Enter score for Test 2: "))
    test3 = float(input("Enter score for Test 3: "))
    test = testAverage(test1, test2, test3)
    
    # Assignment scores
    assignMark = float(input("Enter score for the Assignment: "))
    assignment = assAverage(assignMark)
    
    # Exam score
    examMark = float(input("Enter score for the Exam: "))
    exam = examAverage(examMark)
    
    # Record score
    grade = gradeAverage(test, assignment, exam)
    
    # Store as a nested dictionary (not in a list)
    studentRecord[name] = {
        "Student ID": studentNumber,
        "Grade": grade,
        "Full Results": {
            "Test Average": test,
            "Assignment Average": assignment,
            "Exam Average": exam
        }
    }
    
    finished = input("Student Recorded, would you like to continue? (y/n): ")

print("\nFinal Student Records:")
for student, details in studentRecord.items():
    print(f"\n{student}:")
    print(f"  Student ID: {details['Student ID']}")
    print(f"  Grade: {details['Grade']}")
    print("  Full Results:")
    print(f"    Test Average: {details['Full Results']['Test Average']}")
    print(f"    Assignment Average: {details['Full Results']['Assignment Average']}")
    print(f"    Exam Average: {details['Full Results']['Exam Average']}")

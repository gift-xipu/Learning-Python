from classes.student import Student

def main():
    complete = 'n'
    while complete == 'n':
        name = input("Enter Students Name: ")
        studentNumber = input(f"Enter Student Number for {name}")
        test_score = []
        assignment_score = []
        #record for tests
        for i in range(3):
            scores = float(input(f"Enter score for Test {i+1}"))
            test_score.append(scores)
        #record for assignment
        for i in range(2):
            scores = float(input(f"Enter score for Assignment {i+1}"))
            assignment_score.append(scores)
        #record for exam
        exam_score = float(input("Enter score for the exam"))
        student = Student(name, studentNumber, test_score, assignment_score, exam_score)
        #test average
        test = student.calculateTest()







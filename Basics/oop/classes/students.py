class Student():
    def __init__(self, name, studentID, test, assignment, exam):
        self.name = name
        self.studentID = studentID
        self.test = test
        self.assignment = assignment
        self.exam = exam

    def studentRecord(self, percentage, grade):
        studentData = {
            self.name: {
                "ID": self.studentID,
                "Percentage": percentage,
                "Grade": grade
            }
        }
        print("\nStudent Record:", studentData)  # Display the stored record
        return studentData

    def calculateTest(self):
        average = (sum(self.test) / 300) * 30  # Fix: Sum the test scores before division
        return average

    def calculateAssignment(self):
        average = (sum(self.assignment) / 200) * 30  # Fix: Sum assignment scores before division
        return average

    def calculateExam(self):
        average = (self.exam / 100) * 40
        return average

    def finalMark(self):
        return self.calculateTest() + self.calculateAssignment() + self.calculateExam()

    def studentGrade(self, final):
        if final >= 75:
            return "Passed with Distinction"
        elif final >= 50:
            return "Pass"
        else:
            return "Fail"

import csv

class StudentData:

    FILE_PATH = "Students.csv"
    #writing student to FILE_PATH
    @staticmethod
    def create_student(student):
        with open(StudentData.FILE_PATH,"w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Student ID","Name","Grade","Mark"])
            writer.writerows(student)
    
    @staticmethod



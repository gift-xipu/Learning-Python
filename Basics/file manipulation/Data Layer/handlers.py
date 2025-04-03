#import csv

#base class for all files
#standard for all csv file
class CSVHandler:
    def __init__ (self, FILE_PATH):
        self.FILE_PATH = FILE_PATH

    def read_file():
        pass
    def write_file():
        pass
    def append_file(entry):
        pass

class StudentFileData(CSVHandler):
    def __init__(self):
        super().__init__("students.csv")

    def get_student_by_id(student_id):
        pass

    def get_students_by_course(course_id):
        pass

    def add_student(student):
        pass

    def update_student(student_id):
        pass

class CourseFileData(CSVHandler):
    def __init__ (self):
        self().__init__("courses.csv")


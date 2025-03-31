from classes.students import Student

def main():
    while True:
        name = input("Enter Student's Name: ").strip()
        studentNumber = input(f"Enter Student Number for {name}: ").strip()

        test_score = []
        assignment_score = []

        # Record test scores
        for i in range(3):
            while True:
                try:
                    score = float(input(f"Enter score for Test {i+1}: "))
                    test_score.append(score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

        # Record assignment scores
        for i in range(2):
            while True:
                try:
                    score = float(input(f"Enter score for Assignment {i+1}: "))
                    assignment_score.append(score)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

        # Record exam score
        while True:
            try:
                exam_score = float(input("Enter score for the exam: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Create student object
        student = Student(name, studentNumber, test_score, assignment_score, exam_score)

        # Calculate and display results
        percent = student.finalMark()
        grade = student.studentGrade(percent)
        student.studentRecord(percent, grade)

        # Ask if the user wants to continue
        again = input("\nStudent Recorded! Would you like to add more? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()

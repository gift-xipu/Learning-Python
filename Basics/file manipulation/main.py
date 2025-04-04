def searchStudent(student_id):
    pass


def main():
    while True:
        print("\nInformation Systems Student Record System")
        print("1. Search for a Student")
        print("2. Add a new Student to the system")
        print("3. Update Student Detail")
        print("4. Record Student Mark")
        print("5. Read Mark")
        print("Enter 'q' to quit.")

        choice = input("Enter your choice (1-5) or 'q': ").strip().lower()

        match choice:
            case "1":
                print("Searching for a student...")
            case "2":
                print("Adding a new student...")
            case "3":
                print("Updating student details...")
            case "4":
                print("Recording student mark...")
            case "5":
                print("Reading student mark...")
            case "q":
                print("Exiting system. Goodbye!")
                break
            case _:
                print("Invalid input. Please enter a number between 1-5 or 'q' to quit.")

if __name__ == "__main__":
    main()


def main():
    system_on = True
    while system_on:

        print("Student Record System")
        print("Hello! What would you like to do today?")
        print("    1. Search for a Student")
        print("    2. Add a new Student to the system")
        print("    3. Update Student Detail")
        print("    4. Record Student Mark")
        print("    5. Read Mark")
        
        # Get user choice
        choice = input("Enter your choice (1-5) or 'q' to quit: ")
        
        if choice == 'q':
            system_on = False
            print("Exiting system. Goodbye!")

if __name__ == "__main__":
    main()

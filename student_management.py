# Dictionary to store all students
students_dict = {}

def display_menu():
    print("1. Press 1 for Counselor")
    print("2. Press 2 for Faculty")
    print("3. Press 3 for Student")

def execute_option(option):
    if option == 1:
        print("Executing Counselor option")
        counselor_logic()
    elif option == 2:
        print("Executing Faculty option")
        faculty_logic()
    elif option == 3:
        print("Executing Student option")
        student_logic()
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

def counselor_logic():
    print("Counselor Menu:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View All Students")
    print("4. View Specific Student")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            remove_student()
        elif choice == 3:
            view_all_students()
        elif choice == 4:
            view_specific_student()
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_student():
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    # Check if the student_id already exists in the dictionary
    if student_id in students_dict:
        print(f"Student with ID {student_id} already exists.")
    else:
        students_dict[student_id] = {'Name': student_name, 'ID': student_id}
        print(f"Student {student_name} added.")

def remove_student():
    student_id = input("Enter student ID to remove: ")
    
    # Check if the student_id exists in the dictionary
    if student_id in students_dict:
        del students_dict[student_id]
        print(f"Student with ID {student_id} removed.")
    else:
        print(f"Student with ID {student_id} not found.")

def view_all_students():
    print("Displaying all students:")
    for student_id, student_info in students_dict.items():
        print(f"ID: {student_id}, Name: {student_info['Name']}")

def view_specific_student():
    student_id = input("Enter student ID to view: ")
    
    # Check if the student_id exists in the dictionary
    if student_id in students_dict:
        student_info = students_dict[student_id]
        print(f"ID: {student_id}, Name: {student_info['Name']}")
    else:
        print(f"Student with ID {student_id} not found.")

def faculty_logic():
    # Add code for faculty-related functionality
    print("Faculty logic goes here.")

def student_logic():
    # Add code for student-related functionality
    print("Student logic goes here.")

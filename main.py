from student_management import execute_option, display_menu

if __name__ == "__main__":
    display_menu()
    try:
        user_option = int(input("Enter a role id: "))
        execute_option(user_option)
    except ValueError:
        print("Invalid input. Please enter a number.")

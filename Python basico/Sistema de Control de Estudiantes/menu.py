import actions
import data

def student_control_menu():
    students = []
    while True:
        option = input("""
Welcome, select an option:
    1. Enter a new student
    2. See all students
    3. See top 3 students by average score
    4. See average score of all students
    5. Export all data to CSV
    6. Import data from CSV
    7. Exit
    """)
        try:
            option = int(option)
            if option == 1:
                students = actions.add_new_student(students)
            elif option == 2:
                actions.see_all_students(students)
            elif option == 3:
                actions.get_top_3_students(students)
            elif option == 4:
                actions.get_total_average_score(students)
            elif option == 5:
                data.export_data_to_csv(students)
            elif option == 6:
                students = data.import_data_from_csv(students)
            elif option == 7:
                print("Goodbye!")
                break
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input, please enter a number.")
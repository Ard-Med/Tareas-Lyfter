
def add_new_student(students):
    student = input("Enter the student name: ")
    section = input("Enter the student section: ")
    spanish_score = get_valid_score("Spanish")
    english_score = get_valid_score("English")
    social_score = get_valid_score("Social")
    science_score = get_valid_score("Science")
    average = round((spanish_score + english_score + social_score + science_score) / 4, 2)
    students.append({
        "Student Name": student,
        "Student Section": section,
        "Spanish Score": spanish_score,
        "English Score": english_score,
        "Social Score": social_score,
        "Science Score": science_score,
        "Student Average": average
    })
    print("Student added successfully.")
    return students


def get_valid_score(subject):
    while True:
        try:
            score = int(input(f"Enter the {subject} score: "))
            if 0 <= score <= 100:
                return score
            print("Invalid score, enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def see_all_students(students):
    if not students:
        print("No students registered.")
        return
    for student in students:
            print("Student Name: ", student["Student Name"])
            print("Student Section: ", student["Student Section"])
            print("Spanish Score: ", student["Spanish Score"])
            print("English Score: ", student["English Score"])
            print("Social Score: ", student["Social Score"])
            print("Science Score: ", student["Science Score"])
            print("Student Average: ", student["Student Average"])
            print("--------")


def get_total_average_score(students):
    if not students:
        print("No students registered.")
        return
    total = sum(student["Student Average"] for student in students)
    print(f"The average score of all students is: {round(total / len(students), 2)}")

def get_average(student):
    return student["Student Average"]

def get_top_3_students(students):
    if not students:
        print("No students registered.")
        return
    sorted_students = sorted(students, key=get_average, reverse=True)
    top_3 = sorted_students[:3]
    print("Top 3 students by average score:")
    for i, student in enumerate(top_3, start=1):
        print(f"{i}. {student['Student Name']} - Average: {student['Student Average']}")
import re

def is_valid_name(name):
    return bool(name.strip()) and not any(char.isdigit() for char in name)

def is_valid_section(section):
    return bool(re.match(r"^\d{2}[A-Za-z]$", section))

def student_exists(students, name, section):
    return any(
        s["Student Name"].lower() == name.lower() and
        s["Student Section"].lower() == section.lower()
        for s in students
    )

def add_new_student(students):
    while True:
        name = input("Enter the student name: ").strip()
        if not is_valid_name(name):
            print("Invalid name. It cannot be empty or contain numbers.")
            continue
        break

    while True:
        section = input("Enter the student section (e.g. 10A, 11B): ").strip()
        if not is_valid_section(section):
            print("Invalid section. It must follow the format '10A', '11B', etc.")
            continue
        break

    if student_exists(students, name, section):
        print("A student with that name and section already exists.")
        return students

    spanish_score = get_valid_score("Spanish")
    english_score = get_valid_score("English")
    social_score = get_valid_score("Social")
    science_score = get_valid_score("Science")
    average = round((spanish_score + english_score + social_score + science_score) / 4, 2)

    students.append({
        "Student Name": name,
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
    total = sum(float(student["Student Average"]) for student in students)
    print(f"The average score of all students is: {round(total / len(students), 2)}")


def get_average(student):
    return float(student["Student Average"])


def get_top_3_students(students):
    if not students:
        print("No students registered.")
        return
    sorted_students = sorted(students, key=get_average, reverse=True)
    top_3 = sorted_students[:3]
    print("Top 3 students by average score:")
    for i, student in enumerate(top_3, start=1):
        print(f"{i}. {student['Student Name']} - Average: {student['Student Average']}")


def delete_student(students):
    if not students:
        print("No students registered.")
        return students

    name = input("Enter the student name to delete: ").strip()
    section = input("Enter the student section: ").strip()

    if not student_exists(students, name, section):
        print("Student not found.")
        return students

    confirm = input(f"Are you sure you want to delete {name} from section {section}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return students

    students = [
        s for s in students
        if not (s["Student Name"].lower() == name.lower() and s["Student Section"].lower() == section.lower())
    ]
    print("Student deleted successfully.")
    return students


def see_failing_students(students):
    if not students:
        print("No students registered.")
        return

    subjects = ["Spanish Score", "English Score", "Social Score", "Science Score"]
    failing = []

    for student in students:
        failed_subjects = [s for s in subjects if int(float(student[s])) < 60]
        if failed_subjects:
            failing.append((student, failed_subjects))

    if not failing:
        print("No failing students.")
        return

    print("Failing students:")
    for student, failed_subjects in failing:
        print(f"\nName: {student['Student Name']} | Section: {student['Student Section']}")
        for subject in failed_subjects:
            print(f"  {subject}: {student[subject]}")
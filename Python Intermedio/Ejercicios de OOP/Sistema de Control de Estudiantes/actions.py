import re

class Student:
    def __init__(self, name, section, spanish_score, english_score, social_score, science_score):
        self.name = name
        self.section = section
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.social_score = social_score
        self.science_score = science_score
        self.average = round((spanish_score + english_score + social_score + science_score) / 4, 2)
        
    def to_dict(self):
        return {
        "Student Name": self.name,
        "Student Section": self.section,
        "Spanish Score": self.spanish_score,
        "English Score": self.english_score,
        "Social Score": self.social_score,
        "Science Score": self.science_score,
        "Student Average": self.average
    }


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
    students.append(Student(name, section, spanish_score, english_score, social_score, science_score))
    print("Student added successfully.")
    return students


def is_valid_name(name):
    return bool(name.strip()) and not any(char.isdigit() for char in name)


def is_valid_section(section):
    return bool(re.match(r"^\d{2}[A-Za-z]$", section))


def student_exists(students, name, section):
    return any(
        s.name.lower() == name.lower() and
        s.section.lower() == section.lower()
        for s in students
    )


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
        print("Student Name: ", student.name)
        print("Student Section: ", student.section)
        print("Spanish Score: ", student.spanish_score)
        print("English Score: ", student.english_score)
        print("Social Score: ", student.social_score)
        print("Science Score: ", student.science_score)
        print("Student Average: ", student.average)
        print("--------")


def get_total_average_score(students):
    if not students:
        print("No students registered.")
        return
    total = sum(float(student.average) for student in students)
    print(f"The average score of all students is: {round(total / len(students), 2)}")


def get_average(student):
    return float(student.average)


def get_top_3_students(students):
    if not students:
        print("No students registered.")
        return
    sorted_students = sorted(students, key=get_average, reverse=True)
    top_3 = sorted_students[:3]
    print("Top 3 students by average score:")
    for i, student in enumerate(top_3, start=1):
        print(f"{i}. {student.name} - Average: {student.average}")


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
        if not (s.name.lower() == name.lower() and s.section.lower() == section.lower())
    ]
    print("Student deleted successfully.")
    return students


def see_failing_students(students):
    if not students:
        print("No students registered.")
        return
    failing = []
    for student in students:
        subjects = {
            "Spanish": student.spanish_score,
            "English": student.english_score,
            "Social": student.social_score,
            "Science": student.science_score
        }
        failed_subjects = [(subj, score) for subj, score in subjects.items() if score < 60]
        if failed_subjects:
            failing.append((student, failed_subjects))
    if not failing:
        print("No failing students.")
        return
    print("Failing students:")
    for student, failed_subjects in failing:
        print(f"\nName: {student.name} | Section: {student.section}")
        for subject, score in failed_subjects:
            print(f"  {subject}: {score}")
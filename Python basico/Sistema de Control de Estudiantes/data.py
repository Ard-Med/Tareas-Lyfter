
import os
import csv

def set_table_headers():
    return (
        "Student Name",
        "Student Section",
        "Spanish Score",
        "English Score",
        "Social Score",
        "Science Score",
        "Student Average",
    )

def export_data_to_csv(students, filename="StudentControl.csv"):
    headers = set_table_headers()
    file_exists = os.path.exists(filename)
    file_check = "a" if file_exists else "w"
    with open(filename, file_check, encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerows(students)
    print("Data exported successfully.")

def import_data_from_csv(students, filename="StudentControl.csv"):
    if not os.path.exists(filename):
        print("No CSV file found.")
        return students
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    print("Data imported successfully.")
    return students
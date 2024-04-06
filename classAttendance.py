import pickle
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
def add_student(students):
    name = input("Enter student's name: ")
    student = {"name": name, "attendance": {'Monday': '', 'Tuesday': '', 'Wednesday': '', 'Thursday': '', 'Friday': ''}}
    students.append(student)
def take_attendance(students):
    day = input("Enter the day of the week (Monday to Friday): ")
    for student in students:
        attendance = input(f"Enter attendance (P for present, A for absent, T for tardy) for {student['name']}: ")
        student['attendance'][day] = attendance
def edit_attendance(students):
    name = input("Enter student's name: ")
    for student in students:
        if student['name'] == name:
            day = input("Enter the day of the week to edit (Monday to Friday): ")
            attendance = input(
                f"Enter new attendance (P for present, A for absent, T for tardy) for {student['name']} on {day}: ")
            student['attendance'][day] = attendance
def print_student_attendance(students):
    name = input("Enter student's name: ")
    for student in students:
        if student['name'] == name:
            print(f"{student['name']}'s attendance for the week:")
            for day, att in student['attendance'].items():
                print(f"{day}: {att}")
def print_class_attendance(students):
    print("Class attendance for the week:")
    for student in students:
        print(f"{student['name']}:")
        for day, att in student['attendance'].items():
            print(f"{day}: {att}")
        print()
def save_data(students):
    with open('attendance_data.pkl', 'wb') as file:
        pickle.dump(students, file)
def load_data():
    try:
        with open('attendance_data.pkl', 'rb') as file:
            students = pickle.load(file)
            print("Student data loaded")
            return students
    except FileNotFoundError:
        print("No data found. Please add students first.")
        return []
students = []
menu = ConsoleMenu("Attendance Program Menu", "Select an option:")
menu.append_item(FunctionItem("Add Student", add_student, [students]))
menu.append_item(FunctionItem("Take Attendance", take_attendance, [students]))
menu.append_item(FunctionItem("Edit Attendance", edit_attendance, [students]))
menu.append_item(FunctionItem("Print Student Attendance", print_student_attendance, [students]))
menu.append_item(FunctionItem("Print Class Attendance", print_class_attendance, [students]))
menu.append_item(FunctionItem("Save Attendance Data", save_data, [students]))
menu.append_item(FunctionItem("Load Attendance Data", load_data))
menu.show()

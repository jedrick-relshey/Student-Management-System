# ==========================================================
# STUDENT RECORD MANAGEMENT SYSTEM
# IT 31 - Data Structures and Algorithm
# Prelims Performance Task
# ==========================================================

students = []

# ==========================================================
# MAIN MENU
# ==========================================================

def main_menu():
    while True:
        print("\n" + "=" * 55)
        print("      STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 55)
        print("[1] Add Student Record")
        print("[2] View Student Records")
        print("[3] Search Student")
        print("[4] Update Student Record")
        print("[5] Delete Student Record")
        print("[6] Display Class Statistics")
        print("[7] Exit")
        print("=" * 55)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            display_statistics()

        elif choice == "7":
            print("\n========================================")
            print(" Thank you for using the system!")
            print(" Student Record Management System")
            print(" Goodbye!")
            print("========================================")
            break
        else:
            print("\nInvalid menu choice.")

# ==========================================================
# VALIDATIONS
# ==========================================================

def validate_student_id():
    while True:
        student_id = input("Student ID (9 digits): ").strip()

        if not student_id.isdigit():
            print("Student ID must contain numbers only.")
            continue

        if len(student_id) != 9:
            print("Student ID must be exactly 9 digits.")
            continue

        duplicate = False

        for student in students:
            if student["id"] == student_id:
                duplicate = True
                break

        if duplicate:
            print("Student ID already exists.")
            continue
        return student_id


def validate_name(message, required=True):
    while True:
        name = input(message).strip()
        if required and name == "":
            print("This field is required.")
            continue
        if name == "":
            return ""
        valid = True

        for letter in name:
            if not (letter.isalpha() or letter == " "):
                valid = False
                break

        if not valid:
            print("Letters and spaces only.")
            continue
        return name.title()

def validate_course():
    while True:
        course = input("Course: ").strip().upper()
        if course == "":
            print("Course is required.")
            continue
        return course

def validate_section():

    while True:
        section = input("Section: ").strip().upper()

        if section == "":
            print("Section is required.")
            continue
        return section

def validate_grade():
    while True:
        try:
            grade = float(input("Final Grade: "))
            if grade < 0 or grade > 100:
                print("Grade must be from 0 to 100.")
                continue
            return grade
        except ValueError:
            print("Numeric values only.")

# ==========================================================
# ADD STUDENT
# ==========================================================

def add_student():
    print("\n" + "=" * 55)
    print("ADD STUDENT RECORD")
    print("=" * 55)

    student = {
        "id": validate_student_id(),
        "last_name": validate_name("Last Name: "),
        "first_name": validate_name("First Name: "),
        "middle_name": validate_name("Middle Name (Optional): ", required=False),
        "course": validate_course(),
        "section": validate_section(),
        "grade": validate_grade()
    }

    students.append(student)
    students.sort(key=lambda x: x["id"])
    print("\nStudent record added successfully!")
    input("\nPress Enter to continue...")

def view_students():
    print("\n"+"="*100)
    print("STUDENT RECORDS")
    print("="*100)
    if not students:
        print("No student records found.")
    else:
        print(f"{'ID':<12}{'NAME':<35}{'COURSE':<12}{'SECTION':<10}{'GRADE':<8}REMARKS")
        print("-"*100)
        for s in students:
            name=f"{s['last_name']}, {s['first_name']} {s['middle_name']}".strip()
            remarks="PASS" if s["grade"]>=75 else "FAIL"
            print(f"{s['id']:<12}{name:<35}{s['course']:<12}{s['section']:<10}{s['grade']:<8.2f}{remarks}")
    input("\nPress Enter to continue...")

def display_student(student):
    print("="*55)
    for k,v in [("Student ID",student["id"]),("Last Name",student["last_name"]),("First Name",student["first_name"]),("Middle Name",student["middle_name"]),("Course",student["course"]),("Section",student["section"]),("Final Grade",student["grade"])]:
        print(f"{k:<13}: {v}")
    print(f"Remarks      : {'PASS' if student['grade']>=75 else 'FAIL'}")
    print("="*55)

def search_student():
    c=input("[1] ID\n[2] Last Name\nChoice: ")
    found=False
    if c=="1":
        key=input("Enter Student ID: ").strip()
        for s in students:
            if s["id"]==key:
                display_student(s); found=True; break
    elif c=="2":
        key=input("Enter Last Name: ").strip().lower()
        for s in students:
            if s["last_name"].lower()==key:
                display_student(s); found=True
    if not found: print("Student Record Not Found")
    input("\nPress Enter to continue...")

def update_student():
    sid=input("Enter Student ID: ").strip()
    for s in students:
        if s["id"]==sid:
            display_student(s)
            s["last_name"]=validate_name("Last Name: ")
            s["first_name"]=validate_name("First Name: ")
            s["middle_name"]=validate_name("Middle Name (Optional): ",required=False)
            s["course"]=validate_course()
            s["section"]=validate_section()
            s["grade"]=validate_grade()
            print("Updated successfully.")
            input("\nPress Enter to continue...")
            return
    print("Student Record Not Found")
    input("\nPress Enter to continue...")

def delete_student():
    sid=input("Enter Student ID: ").strip()
    for s in students:
        if s["id"]==sid:
            display_student(s)
            if input("Delete this record? (Y/N): ").upper()=="Y":
                students.remove(s)
                print("Deleted.")
            else:
                print("Cancelled.")
            input("\nPress Enter to continue...")
            return
    print("Student Record Not Found")
    input("\nPress Enter to continue...")

def display_statistics():
    if not students:
        print("No student records found.")
    else:
        grades=[s["grade"] for s in students]
        print(f"Total Number of Students : {len(students)}")
        print(f"Highest Grade            : {max(grades):.2f}")
        print(f"Lowest Grade             : {min(grades):.2f}")
        print(f"Average Grade            : {sum(grades)/len(grades):.2f}")
        print(f"Passed Students          : {sum(g>=75 for g in grades)}")
        print(f"Failed Students          : {sum(g<75 for g in grades)}")
    input("\nPress Enter to continue...")

main_menu()
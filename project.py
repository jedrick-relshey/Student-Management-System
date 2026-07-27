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

    if len(students) == 0:
        print("No student records found.")
        input("\nPress Enter to continue...")
        return

    print(f"{'ID':<12}{'NAME':<35}{'COURSE':<12}{'SECTION':<10}{'GRADE':<10}{'REMARKS'}")
    print("-" * 100)

    for student in students:

        fullname = f"{student['last_name']}, {student['first_name']}"

        if student["middle_name"] != "":
            fullname += f" {student['middle_name']}"

        if student["grade"] >= 75:
            remarks = "PASS"
        else:
            remarks = "FAIL"

        print(
            f"{student['id']:<12}"
            f"{fullname:<35}"
            f"{student['course']:<12}"
            f"{student['section']:<10}"
            f"{student['grade']:<10.2f}"
            f"{remarks}"
        )

    input("\nPress Enter to continue...")


# ==========================================================
# SEARCH STUDENT
# ==========================================================

def search_student():
    print("\n" + "=" * 55)
    print("SEARCH STUDENT")
    print("=" * 55)

    print("[1] Search by Student ID")
    print("[2] Search by Last Name")

    choice = input("Enter choice: ")

    found = False

    if choice == "1":

        search_id = input("Enter Student ID: ").strip()

        for student in students:

            if student["id"] == search_id:
                display_student(student)

                found = True
                break

    elif choice == "2":

        search_name = input("Enter Last Name: ").strip().lower()

        for student in students:

            if student["last_name"].lower() == search_name:
                display_student(student)

                found = True

    else:

        print("Invalid choice.")
        input("\nPress Enter to continue...")
        return

    if not found:
        print("\nStudent Record Not Found")

    input("\nPress Enter to continue...")


# ==========================================================
# DISPLAY SINGLE STUDENT
# ==========================================================

def display_student(student):
    print("\n" + "=" * 55)

    print(f"Student ID   : {student['id']}")
    print(f"Last Name    : {student['last_name']}")
    print(f"First Name   : {student['first_name']}")
    print(f"Middle Name  : {student['middle_name']}")
    print(f"Course       : {student['course']}")
    print(f"Section      : {student['section']}")
    print(f"Final Grade  : {student['grade']}")

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:
            print("\nCurrent Student Information")
            display_student(student)

            print("\nEnter New Information")

            student["last_name"] = validate_name("Last Name: ")
            student["first_name"] = validate_name("First Name: ")
            student["middle_name"] = validate_name(
                "Middle Name (Optional): ",
                required=False
            )
            student["course"] = validate_course()
            student["section"] = validate_section()
            student["grade"] = validate_grade()

            print("\nStudent record updated successfully!")

            input("\nPress Enter to continue...")
            return

    print("\nStudent Record Not Found")
    input("\nPress Enter to continue...")


# ==========================================================
# DELETE STUDENT RECORD
# ==========================================================

def delete_student():
    print("\n" + "=" * 55)
    print("DELETE STUDENT RECORD")
    print("=" * 55)

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Information")
            display_student(student)

            confirm = input("\nDelete this record? (Y/N): ").upper()

            if confirm == "Y":

                students.remove(student)

                print("\nStudent record deleted successfully!")

            else:

                print("\nDelete cancelled.")

            input("\nPress Enter to continue...")
            return

    print("\nStudent Record Not Found")
    input("\nPress Enter to continue...")

    if student["grade"] >= 75:
        print("Remarks      : PASS")
    else:
        print("Remarks      : FAIL")

    print("=" * 55)

    student_id = validate_student_id()

    last_name = validate_name("Last Name: ")

    first_name = validate_name("First Name: ")

    middle_name = validate_name(
        "Middle Name (Optional): ",
        required=False
    )

    course = validate_course()

    section = validate_section()

    grade = validate_grade()

    student = {

        "id": student_id,
        "last_name": last_name,
        "first_name": first_name,
        "middle_name": middle_name,
        "course": course,
        "section": section,
        "grade": grade

    }

    students.append(student)

    students.sort(key=lambda x: x["id"])

    print("\nStudent record added successfully!")

    input("\nPress Enter to continue...")

# ==========================================================
# DISPLAY CLASS STATISTICS
# ==========================================================

def display_statistics():

    print("\n" + "=" * 55)
    print("CLASS STATISTICS")
    print("=" * 55)

    if len(students) == 0:
        print("No student records found.")
        input("\nPress Enter to continue...")
        return

    highest = students[0]["grade"]
    lowest = students[0]["grade"]

    total_grade = 0
    passed = 0
    failed = 0

    for student in students:

        grade = student["grade"]

        total_grade += grade

        if grade > highest:
            highest = grade

        if grade < lowest:
            lowest = grade

        if grade >= 75:
            passed += 1
        else:
            failed += 1

    average = total_grade / len(students)

    print(f"Total Number of Students : {len(students)}")
    print(f"Highest Grade           : {highest:.2f}")
    print(f"Lowest Grade            : {lowest:.2f}")
    print(f"Average Grade           : {average:.2f}")
    print(f"Passed Students         : {passed}")
    print(f"Failed Students         : {failed}")

    input("\nPress Enter to continue...")

# ==========================================================
# START PROGRAM
# ==========================================================

main_menu()


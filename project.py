# ==========================================================
# STUDENT RECORD MANAGEMENT SYSTEM
# IT 31 - Data Structures and Algorithm
# Prelims Performance Task
# Programmer Diaz, Timothy Vrent A
# Members
# Jedrick Relshey Miclat
# chris Ivan Vital Tolentino
#

# ==========================================================

students = []

# ==========================================================
# MAIN MENU
# ==========================================================

#Display the Main Menu at allows the user to choose.
def main_menu():

    #Eto naman yung loop para sa mga menu.
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

        #Input para sa pag pili ng user sa main menu.
        choice = input("Enter your choice: ")

        #If and elif statement para i call ang choice Variable form 1 to 7.
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
            print("\n========================================================")
            print(" Thank you for using the Student Record Management System!")
            print("==========================================================")
            break
        else:
            print("\nInvalid menu choice.")

# VALIDATIONS

#Validate the Student ID by user
def validate_student_id():
    #Keep asking until a valid Student ID is entered.
    while True:
        # Get Student ID Form the User.
        student_id = input("Student ID (9 digits): ").strip()

        #Check if the user input numbers only.
        if not student_id.isdigit():
            print("Student ID must contain numbers only.")
            continue

        #Check if yung Student ID is 9 Digit.
        if len(student_id) != 9:
            print("Student ID must be exactly 9 digits.")
            continue

        #Check if Student ID is already Exists. If yes then print the "Student ID is already exists."
        duplicate = False

        for student in students:
            if student["id"] == student_id:
                duplicate = True
                break

        if duplicate:
            print("Student ID is already exists.")
            continue
        return student_id

# Validate the name entered by the user
def validate_name(message, required=True):
    # Asking until a valid name is entered
    while True:
        #Get user input.
        name = input(message).strip()
        if required and name == "":
            print("This field is required.")
            continue

        #Allow the empty value id ang field is optional.
        if name == "":
            return ""
        # Flag to check if the name is valid
        valid = True

        #Allow only letter and space
        for letter in name:
            if not (letter.isalpha() or letter == " "):
                valid = False
                break

        if not valid:
            print("Letters and spaces only.")
            continue
        # Return the name with proper capitalization
        return name.title()

def validate_course():
    #ASking until the user enter Course.
    while True:
        course = input("Course: ").strip().upper()
        #Check if the user input a valid Course if not then print the "Course is required."
        if course == "":
            print("Course is required.")
            continue

        return course

def validate_section():
    #Asking the user to input a Section.
    while True:
        section = input("Section: ").strip().upper()
        #If User didn't input a Section show this program
        if section == "":
            print("Section is required.")
            continue

        return section

# Validate the final grade entered by the user
def validate_grade():
    # Return a valid grade between 0 and 100.
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

# Collects and validates student information before saving it.
def add_student():

    #Disple the add student Record Header
    print("\n" + "=" * 55)
    print("ADD STUDENT RECORD")
    print("=" * 55)

    # Create a dictionary containing the student information
    student = {

        #Get and validate the student Id
        "id": validate_student_id(),

        #Get and validate the student name details.
        "last_name": validate_name("Last Name: "),
        "first_name": validate_name("First Name: "),
        "middle_name": validate_name("Middle Name (Optional): ", required=False),

        # Get and validate the student course, section, and grade
        "course": validate_course(),
        "section": validate_section(),
        "grade": validate_grade()
    }

    #adding a new student record to the Student list.
    students.append(student)
    # Sort student records by Student ID
    students.sort(key=lambda x: x["id"])
    # Display confirmation message after successful addition
    print("\nStudent record added successfully!")
    # Pause the program until the user presses Enter
    input("\nPress Enter to continue...")

# Display all student records with their details and academic remarks.
def view_students():
    print("\n"+"="*100)
    print("STUDENT RECORDS")
    print("="*100)

    #Check if there are available student record if not then print then message.
    if not students:
        print("No student records found.")

    else:
        print(f"{'ID':<12}{'NAME':<35}{'COURSE':<12}{'SECTION':<10}{'GRADE':<8}REMARKS")
        print("-"*100)

        #Using for loop display each student information
        for s in students:
            name=f"{s['last_name']}, {s['first_name']} {s['middle_name']}".strip()
            remarks="PASS" if s["grade"]>=75 else "FAIL"

            print(f"{s['id']:<12}{name:<35}{s['course']:<12}{s['section']:<10}{s['grade']:<8.2f}{remarks}")

    input("\nPress Enter to continue...")

# Display the complete information of a selected student record.
def display_student(student):
    print("="*55)

    # Display student details using key-value pairs
    for k,v in [("Student ID",student["id"]),
                ("Last Name",student["last_name"]),
                ("First Name",student["first_name"]),
                ("Middle Name",student["middle_name"]),
                ("Course",student["course"]),
                ("Section",student["section"]),
                ("Final Grade",student["grade"])
    ]:

        print(f"{k:<13}: {v}")

    # Display academic remark based on final grade
    print(f"Remarks      : {'PASS' if student['grade']>=75 else 'FAIL'}")
    print("="*55)

# Search for a student record using Student ID or Last Name.
def search_student():
    c=input("[1] ID\n[2] Last Name\nChoice: ")
    found=False

    # Search student by ID
    if c=="1":
        key=input("Enter Student ID: ").strip()
        for s in students:
            if s["id"]==key:
                display_student(s)
                found=True
                break

    # Search student by Last Name
    elif c=="2":
        key=input("Enter Last Name: ").strip().lower()
        for s in students:
            if s["last_name"].lower()==key:
                display_student(s)
                found=True

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
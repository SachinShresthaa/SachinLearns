students = []


def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)

        print("\nStudent added successfully!")

    except ValueError:
        print("\nPlease enter valid numbers for ID and Age.")


def view_students():
    if len(students) == 0:
        print("\nNo student records found.")
        return

    print("\n----- Student Records -----")

    for student in students:
        print(f"""
ID: {student["id"]}
Name: {student["name"]}
Age: {student["age"]}
Course: {student["course"]}
---------------------------
""")


def search_student():
    try:
        student_id = int(input("Enter Student ID to search: "))

        for student in students:
            if student["id"] == student_id:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                return

        print("\nStudent not found.")

    except ValueError:
        print("\nPlease enter a valid Student ID.")


def delete_student():
    try:
        student_id = int(input("Enter Student ID to delete: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("\nStudent deleted successfully.")
                return

        print("\nStudent not found.")

    except ValueError:
        print("\nPlease enter a valid Student ID.")


while True:

    print("""
==============================
    STUDENT RECORD SYSTEM
==============================

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please try again.")
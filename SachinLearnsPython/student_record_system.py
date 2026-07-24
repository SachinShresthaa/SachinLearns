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

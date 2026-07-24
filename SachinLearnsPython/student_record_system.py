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
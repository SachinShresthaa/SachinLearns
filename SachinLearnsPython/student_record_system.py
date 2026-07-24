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
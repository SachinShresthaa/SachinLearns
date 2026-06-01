def count_eligible_students(attendance_list):
    count = 0
    for attendance in attendance_list:
        if attendance >= 75:
            count += 1
    return count

attendances = []
for i in range(1, 11):
    percentage = float(input(f"Enter attendance percentage of Student {i}: "))
    attendances.append(percentage)

eligible_count = count_eligible_students(attendances)
print("Number of eligible students:", eligible_count)
students = {"Amit": "A", "Priya": "B", "Rahul": "C"}

print("Choose an option:")
print("1. Add a new student")
print("2. Update an existing student's grade")
print("3. Print all student grades")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    students[name] = grade
    print(f"{name} added with grade {grade}")

elif choice == 2:
    name = input("Enter student name to update: ")
    if name in students:
        grade = input("Enter new grade: ")
        students[name] = grade
        print(f"{name}'s grade updated to {grade}")
    else:
        print("Student not found!")

elif choice == 3:
    print("\nStudent Grades:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

else:
    print("Invalid choice!")

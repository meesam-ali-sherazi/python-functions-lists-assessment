# Class Marks Analyzer

# Function to get number of students
def get_student_count():
    while True:
        try:
            count = int(input("Enter number of students: "))

            if count > 0:
                return count
            else:
                print("Enter a number greater than 0.")

        except ValueError:
            print("Please enter a whole number.")


# Function to get valid marks
def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if marks >= 0 and marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")


# Function to calculate average
def calculate_average(marks):
    return sum(marks) / len(marks)


# Create two empty lists
student_names = []
student_marks = []


# Get number of students
total_students = get_student_count()


# Get student names and marks
for i in range(total_students):
    print("\nStudent", i + 1)

    name = input("Enter student name: ").strip().title()
    student_names.append(name)

    marks = get_valid_marks()
    student_marks.append(marks)


# Calculate class results
average = calculate_average(student_marks)
highest = max(student_marks)
lowest = min(student_marks)


# Display class report
print("\n========== CLASS REPORT ==========")

print(f"Class Average: {average:.2f}")
print(f"Highest Marks: {highest:g}")
print("Top Student(s):")

for i in range(total_students):
    if student_marks[i] == highest:
        print(student_names[i], "-", student_marks[i])


print(f"\nLowest Marks: {lowest:g}")
print("Lowest Student(s):")

for i in range(total_students):
    if student_marks[i] == lowest:
        print(student_names[i], "-", student_marks[i])


# Count pass and fail students
passed = 0
failed = 0

for marks in student_marks:
    if marks >= 50:
        passed += 1
    else:
        failed += 1

print(f"\nPassed Students: {passed}")
print(f"Failed Students: {failed}")


# Display students above average
print("\nStudents Above Average:")

for i in range(total_students):
    if student_marks[i] > average:
        print(student_names[i], "-", student_marks[i])


# Sort marks in descending order
sorted_marks = sorted(student_marks, reverse=True)

print("\nMarks in Descending Order:")
print(sorted_marks)

print("==================================")
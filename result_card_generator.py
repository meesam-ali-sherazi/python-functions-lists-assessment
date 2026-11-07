# Student Result Card Generator

# Function to get valid marks
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input("Enter " + subject + " marks: "))

            if marks >= 0 and marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Function to calculate percentage
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


# Function to calculate grade
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# Function to format student name
def format_name(name):
    return name.strip().title()


# Get student information
name = input("Enter student name: ")
name = format_name(name)


# Validate roll number
while True:
    roll_no = input("Enter roll number: ")

    if roll_no.isdigit():
        break
    else:
        print("Invalid roll number! Enter digits only.")


# Get marks in five subjects
english = get_valid_marks("English")
math = get_valid_marks("Math")
computer = get_valid_marks("Computer")
physics = get_valid_marks("Physics")
chemistry = get_valid_marks("Chemistry")


# Calculate total marks
total = english + math + computer + physics + chemistry


# Calculate percentage
percentage = calculate_percentage(total, 500)


# Calculate grade
grade = get_grade(percentage)


# Check final status
if english < 40 or math < 40 or computer < 40 or physics < 40 or chemistry < 40:
    status = "Fail"
else:
    status = "Pass"


# Generate result card
print("\n========== STUDENT RESULT CARD ==========")

print(f"Student Name: {name}")
print(f"Roll Number: {roll_no}")

print("-----------------------------------------")

print(f"English: {english:g}")
print(f"Math: {math:g}")
print(f"Computer: {computer:g}")
print(f"Physics: {physics:g}")
print(f"Chemistry: {chemistry:g}")

print("-----------------------------------------")

print(f"Total Marks: {total:g}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Final Status: {status}")

print("=========================================")
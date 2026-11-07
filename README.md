Python Functions, Strings & Lists Assessment

**Project Overview**

This project contains two Python programs developed for the Functions, Strings, and Lists assessment. These programs use functions, loops, conditional statements, strings, and lists.

**Task 1: Student Result Card Generator**

This program generates a student's result card.

**Features**

- Takes student name and roll number.
- Takes marks in five subjects.
- Validates marks between 0 and 100.
- Checks roll number using "isdigit()".
- Formats student name using "strip()" and "title()".
- Calculates total marks and percentage.
- Assigns grades according to percentage.
- Displays Fail if any subject marks are below 40.

**Functions Used**

- "get_valid_marks(subject)"
- "calculate_percentage(total, max_total)"
- "get_grade(percentage)"
- "format_name(name)"

**Sample Input**

Student Name: Ali Ahmed
Roll Number: 12345
English: 85
Math: 90
Computer: 95
Physics: 80
Chemistry: 75

**Sample Output**

Total Marks: 425/500
Percentage: 85.00%
Grade: A
Final Status: Pass

**Task 2: Class Marks Analyzer**

This program analyzes the marks of multiple students.

**Features**

- Takes the number of students.
- Stores student names and marks in separate lists.
- Validates marks between 0 and 100.
- Calculates class average.
- Finds highest and lowest marks.
- Displays top and lowest students.
- Counts passed and failed students.
- Displays students above average.
- Sorts marks in descending order.

**Functions Used**

- "get_student_count()"
- "get_valid_marks()"
- "calculate_average(marks)"

**Sample Input**

Number of Students: 4

Ali: 85
Ahmed: 90
Sara: 65
Usman: 40

**Sample Output**

Class Average: 70.00
Highest Marks: 90
Top Student(s):
Ahmed - 90.0

Lowest Marks: 40
Lowest Student(s):
Usman - 40.0

Passed Students: 3
Failed Students: 1

Students Above Average:
Ali - 85.0
Ahmed - 90.0

Marks in Descending Order:
[90.0, 85.0, 65.0, 40.0]

**Python Concepts Used**

- Variables and Data Types
- Functions
- Strings
- Lists
- append()
- strip() and title()
- if, elif, else
- for and while loops
- Input Validation
- Built-in Functions: sum(), max(), min(), len(), sorted()

**How to Run the Programs**

**Task 1**

python result_card_generator.py

**Task 2**

python class_marks_analyzer.py

**Project Files**

1. "result_card_generator.py"
2. "class_marks_analyzer.py"
3. "README.md"

**Conclusion**

Both programs demonstrate the practical use of Python functions, strings, lists, loops, and conditional statements.
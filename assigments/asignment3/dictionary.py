"""
for the fourth assignment
A Very Simple Student Grade Tracker

Create a dictionary where keys are student names and values are lists of their test scores
Add functions to:

Add a new student
Add a grade for existing student
Calculate average grade for each student
Find the student with highest average
Display all students and their grades in a formatted table
"""

# Initialize the student grades dictionary
# student_grades = {}
# def add_student(name):
#     """Add a new student to the dictionary."""
#     if name not in student_grades:
#         student_grades[name] = []
#         print(f"Student {name} added.")
#     else:
#         print(f"Student {name} already exists.")
# def add_grade(name, grade):
#     """Add a grade for an existing student."""
#     if name in student_grades:
#         student_grades[name].append(grade)
#         print(f"Added grade {grade} for {name}.")
#     else:
#         print(f"Student {name} not found.")
# def calculate_average(name):
#     """Calculate the average grade for a student."""
#     if name in student_grades and student_grades[name]:
#         avg = sum(student_grades[name]) / len(student_grades[name])
#         return avg
#     return 0
# def student_with_highest_average():
#     """Find the student with the highest average grade."""
#     highest_avg = 0
#     top_student = None
#     for name, grades in student_grades.items():
#         if grades:
#             avg = calculate_average(name)
#             if avg > highest_avg:
#                 highest_avg = avg
#                 top_student = name
#     return top_student, highest_avg
# def display_students(): 
#     print("\n--- Student Grades ---")
#     for name, grades in student_grades.items():
#         avg = calculate_average(name)
#         print(f"{name:10} | Grades: {grades} | Average: {avg:.2f}")
#     print("----------------------\n")
# # Example usage
# add_student("Alice")
# add_student("Bob")
# add_grade("Alice", 85)
# add_grade("Alice", 30)
# add_grade("Bob", 78)    

# print(f"Alice's average: {calculate_average('Alice')}")
# top_student, top_avg = student_with_highest_average()

# -------------------------------
# Student Grade Tracker Program
# -------------------------------

# This dictionary will store students and their grades
# Key = student name (string), Value = list of grades (list of numbers)

students = {}

# Function 1: Add a new student
def add_student(name):
    """
    This function creates a new student in the dictionary.
    If the student already exists, it tells us instead of adding again.
    """
    if name not in students:             # Check if student name does NOT exist
        students[name] = []              # Create a new entry with empty grade list
        print(f"Student {name} added.")
    else:
        print(f"Student {name} already exists.")


# Function 2: Add a grade to an existing student
def add_grade(name, grade):
    """
    This function adds a grade to the student's list of grades.
    If the student does not exist, it gives an error message.
    """
    if name in students:                 # Check if the student exists in dictionary
        students[name].append(grade)     # Add the grade to their grade list
        print(f"Added grade {grade} for {name}.")
    else:
        print(f"Student {name} does not exist.")


# Function 3: Calculate average grade for a student
def average_grade(name):
    """
    This function calculates the average grade for one student.
    Formula: sum of grades ÷ number of grades
    If no grades exist, return 0.
    """
    if name in students and students[name]:   # Ensure student exists AND has grades
        return sum(students[name]) / len(students[name])  # Average formula
    else:
        return 0   # No grades yet, return 0


# Function 4: Find the student with the highest average
def best_student():
    """
    This function finds which student has the highest average.
    Uses the max() function with average_grade as the 'key' to compare.
    """
    if not students:                     # If dictionary is empty, return None
        return None
    return max(students, key=lambda name: average_grade(name))


# Function 5: Display all students with their grades and averages
def display_students():
    """
    This function prints a formatted table of all students,
    their grades, and their average score.
    """
    print("\n--- Student Grades ---")
    for name, grades in students.items():    # Loop through all students
        avg = average_grade(name)            # Calculate average for each student
        # Format: student name (10 spaces wide), grades list, average (2 decimal places)
        print(f"{name:10} | Grades: {grades} | Average: {avg:.2f}")
    print("----------------------\n")


# -------------------------------
# Example Run (Testing the Functions)
# -------------------------------

add_student("emmanuel")   # Add student emmanuel 
add_student("Bob")     # Add student Bob

add_grade("emmanuel", 90)  # Add grades for emmanuel
add_grade("emmanuel", 80)
add_grade("Bob", 70)    # Add grade for Bob

display_students()      # Show all students, grades, and averages

print(f"emmanuel's average: {average_grade('emmanuel'):.2f}")
print(f"Best student: {best_student()}")

"""
or the first assignment
Grade Calculator

Ask user for their score (0-100)
Assign letter grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
Provide encouraging messages based on the grade
Handle invalid input (scores outside 0-100 range)
"""

# Get user input
score = int(input("Enter your score (0-100): "))
if score < 0 or score > 100:
    print("Invalid score. Please enter a number between 0 and 100.")
else:
    # Determine letter grade and message
    if score >= 90:
        grade = 'A'
        message = "YOU TOO DEY DO!"
    elif score >= 80:
        grade = 'B'
        message = "GOOD WORK!"
    elif score >= 70:
        grade = 'C'
        message = "PERFECT!"
    elif score >= 60:
        grade = 'D'
        message = "YOU DID A GOOD JOB BUT......."
    else:
        grade = 'F'
        message = "CYNTHIA OFORIE ...!"
    
    print(f"Your grade is: {grade}. {message}")
"""
assignment 
Adults only
Make a program that will keep running until the user gives an age that is above 18
"""

age = 0
while age <= 18:
    age = int(input("Please enter your age: "))
    if age <= 18:
        print("You must be at least 19 years old to proceed.")
    else:
        print("Access granted. You are old enough!")
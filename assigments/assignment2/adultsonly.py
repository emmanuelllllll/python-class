"""
assignment 
Adults only
Make a program that will keep running until the user gives an age that is above 18
"""

age = int(input("Please enter your age: "))
while age <= 18:
    print("You must be at least 18 years old to proceed.")
    age = int(input("Please enter your age: "))
print("Access granted. You are old enough!")
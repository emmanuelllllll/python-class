"""
assignment 4
Positive only
Make a program that will 
Collect an int input from the user
It should also only stop running until the user gives you a negative number
"""
number = 0
while number >= 0:
    number = int(input("Enter a positive number (negative to stop): "))
    if number >= 0:
        print(f"You entered: {number}")
    else:
        print("Negative number entered, stopping the program.")

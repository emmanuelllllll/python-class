# Assignment 2
"""
it will be a game called odd or even you will ask the user for a number the user will input a number and the program has to say 
whether the number given is odd or even

"""

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
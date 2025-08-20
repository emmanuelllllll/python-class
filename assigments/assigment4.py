# Assignment 4
"""
build a program that gives you the greater of two numbers so the user will input two numbers and the program will return the greater of the two numbers
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"The greater number is {num1}.")
elif num2 > num1:
    print(f"The greater number is {num2}.")
else:
    print("Both numbers are equal.")
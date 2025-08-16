"""
will give the sum, quotitent, product, and diffrence of two numbers 
"""

"""

sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum) #addition
subtraction = num1 - num2

print("The subtraction of", num1, "and", num2, "is:", subtraction)
multiplication = num1 * num2

print("The multiplication of", num1, "and", num2, "is:", multiplication)
division = num1 / num2
print("The division of", num1, "and", num2, "is:", division)
"""


num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
method = input("what method of calculation do you want to perform? (addition, subtraction, multiplication, division): ")
if method == "addition":
    print(f"The sum of {num1} and {num2} is: {num1 + num2}")
elif method == "subtraction":
    print(f"The difference between {num1} and {num2} is: {num1 - num2}")
elif method == "multiplication":
    print(f"The product of {num1} and {num2} is: {num1 * num2}")
elif method == "division":
    print(f"The quotient of {num1} and {num2} is: {num1 / num2}")
print ("Thank you for using the calculator!")

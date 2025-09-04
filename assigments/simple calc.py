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
"""
simple calculator, that two user int inputs and op returns 
sum, diff, qoutient, product
"""

# num1 = int(input("enter the first number: "))
# num2 = int(input("enter the second number: "))
# method = input("what method of calculation do you want to perform? (addition, subtraction, multiplication, division): ")
# if (method.lower()== "addition"):
#     print(f"The sum of {num1} and {num2} is: {num1 + num2}")
# elif (method.lower()== "subtraction"):
#     print(f"The difference between {num1} and {num2} is: {num1 - num2}")
# elif (method.lower() == "multiplication"):
#     print(f"The product of {num1} and {num2} is: {num1 * num2}")
# elif (method.lower() == "division"):
#     if num2 == 0:
#         print("Invalid: Division by zero is not allowed.")
#     else:
#         print(f"The quotient of {num1} and {num2} is: {num1 / num2}")
# print ("Thank you for using the calculator!")


#user inputs, num1 and num2
num1 = int(input("input your first number: "))
num2 = int(input("enter your second number: "))

#operation input
op = input("enter your operation: sum \nproduct \nquotient \ndifference ").lower()

#sum, difference, quotient, product
sum = num1 + num2
difference = num1 - num2
quotient  = num1 / num2
product = num1 * num2


if (op.lower() == "sum"): 
    print(f"this is the sum: {sum}")
elif (op.lower() == "difference"):
    print(f"this is the difference of the two numbers: {difference}")
elif (op.lower() == "quotient"):
    if (num2 == 0):
        print("undefined")
    else:
        print(f"this is the quotient of two numbers: {quotient}")
elif (op.lower() == "product"):
    print(f"this is the product of two numbers: {product}")
else:
    print("invalid operator")



print("end of program")




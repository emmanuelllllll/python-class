"""
first assignment fizzbuzz

you are to build a program that will print out from numbers 1 to 30

now while it prints this out,once it gets to the number 3 or any number divisible by 3 it should print out the word ”fizz” 

if it gets to a number 5 or divisible by 5 it should print out the word “buzz”
"""

number = 1  
end_number = 30 

while number <= end_number:
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number) 
    
    number = number + 1

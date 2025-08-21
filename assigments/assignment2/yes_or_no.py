"""
assignment 6 yes or no 
Simple yes or no
Keep asking the user if he wants to continue
They should choose between y or n
If y. Then keep running he program 
If n then break and end the program
"""

response = ''
while response.lower() != 'n':
    response = input("Do you want to continue? (y/n): ")
    if response.lower() == 'y':
        print("Continuing the program...")
    elif response.lower() == 'n':
        print("Ending the program. Goodbye!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
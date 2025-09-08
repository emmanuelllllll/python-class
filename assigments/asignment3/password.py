"""
for the third assignment
Simple Password Strength Checker

Ask user for a password
Check if it meets criteria: at least 8 characters, has uppercase, lowercase, and numbers
Use loops to count each type of character
Keep asking until they provide a strong password
"""
# Simple Password Strength Checker (easier way)

while True:
 password = input("Enter a password: ")

    # Check conditions directly with built-in functions
 if (len(password) >= 8 
        and any(char.isupper() for char in password) 
        and any(char.islower() for char in password) 
        and any(char.isdigit() for char in password)):
        
        print("Strong password")
        break
 else:
        print("Weak password . Try again.\n")



# Simple Password Strength Checker (using loops to count character types)
# while True:
#     password = input("Enter a password: ")
#     if len(password) < 8:
#         print("Password must be at least 8 characters long. Try again.\n")
#         continue
#     uppercase_count = 0
#     lowercase_count = 0
#     digit_count = 0
#     for char in password:
#         if char.isupper():
#             uppercase_count += 1
#         elif char.islower():
#             lowercase_count += 1
#         elif char.isdigit():
#             digit_count += 1
#     if uppercase_count > 0 and lowercase_count > 0 and digit_count > 0:
#         print("Strong password ✅")
#         break   
#     else:
#         print("Weak password ❌. Try again.\n")
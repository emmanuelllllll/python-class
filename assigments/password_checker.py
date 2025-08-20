# Assignment 3
"""
build a simple password checker if the password isnt MR FRANK it should return access denied
if the password is MR FRANK it should return access granted
"""

password = input("Enter the password: ")
if password == "MR FRANK":
    print("Access granted.")
else:
    print("Access denied. Incorrect password.")
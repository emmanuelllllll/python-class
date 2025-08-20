# Assignment 1
"""
Having aptech as your starting point you are to direct a user to either one of two locations (Abakapa or Emene)
get the users name and the place they want to go to
"""

name = input("What is your name? ")
destination = input("Where would you like to go? (Abakapa/Emene): ")
if destination.lower() == "abakapa":
    print(f"Hello {name}, you are going to take a keke across the road from aptech then stop at holy ghost and take a bus in front of the GiG bus terminal to abakapa. HAVE A SAFE TRIP!!")
elif destination.lower() == "emene":
    print(f"Hello {name}, you are going to take a keke across the road from aptech then stop at holy ghost and take a keke in front of the GiG bus terminal to abakapa when you get there take a bus going to Emene. HAVE A SAFE TRIP!!")
else:
    print("Invalid destination. Please choose either Abakapa or Emene.")







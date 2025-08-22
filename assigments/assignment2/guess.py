"""
assignment2.guess
Guess the Number:
Set a secret number (e.g., 7) and Ask the user to guess the number.
Keep asking until they guess correctly
When guessed right, print "Correct! You win."
"""

secret_number = 10 
guess = None 
while guess != secret_number:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You win!") 
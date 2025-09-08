"""
For the second assignment
A Simple ATM Simulator

Start with a balance of $1000
Ask user what they want to do: check balance, deposit, or withdraw
For deposits: add amount to balance
For withdrawals: check if sufficient funds exist
Display appropriate messages and updated balance
"""

# Initial balance
inmoney = 1000
print("Welcome to the ATM Simulator!")
# Get user input
options = input("What would you like to do? (check/deposit/withdraw): ").lower()
if options == "check":
    print(f"Your current balance is: ${inmoney}")
elif options == "deposit":
    amount = int(input("Enter amount to deposit: $"))
    if amount > 0:
        inmoney += amount
        print(f"Deposited: ${amount}. New balance: ${inmoney}")
    elif options == "withdraw":
     amount = float(input("Enter amount to withdraw: "))
    if amount <= inmoney and amount > 0:
        inmoney -= amount
        print(f"Withdrawal successful! Your new balance is ${inmoney}.")
    else:
        print("Invalid deposit amount.")
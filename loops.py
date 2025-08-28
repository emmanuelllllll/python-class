"""
Loops in Python
=================

Loops are used to execute a block of code repeatedly until a certain condition is met. Python provides two main types
 of loops: `for` loops and `while` loops.
"""

mylist = ["football", "basketball", "tennis", "golf", "hunting","racing"]

counter = 0
for item in mylist:
    counter += 1
    print(item)
    if item == "golf":
        print("this is golf")
    else: 
        continue

print (counter)

# do a simple times table using a for loop

table = 15
for number in range(1, 11):
    result = table * number
    print(f"{table} x {number} = {result}")

# while loop
count = 1
while count <= 10:
    print(f" while loop{table} x {count} = {table * count}")
    count += 1
#break statement
# The break statement is used to exit a loop prematurely when a certain condition is met.
name = "EMMANUEL"
for word in name:
    print(word)

# nested loop
# A nested loop is a loop inside another loop. The inner loop will be executed one time for each iteration of the outer loop.


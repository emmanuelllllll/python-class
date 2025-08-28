"""
lists are used to store multiple items in a single variable.
Lists are created using square brackets [].
if you want to access an item in a list, you can use its index.
example: ["emmanuel", "james", "enoch", "daniel"]
Index:    0          1        2         3
Negative Index: -4        -3       -2        -1
print(classmates[2])  # Output: enoch
print(classmates[0]) # Output: emmanuel
"""
classmates = [ "emmanuel", "james", "enoch", "daniel" ]
print(classmates[2])  # Output: enoch
print(classmates[0]) # Output: emmanuel

con = list(("emmanuel", "james", "enoch", "daniel")) # we use list() constructor to create a list because the list() 
#constructor allows us to create a list from any iterable object, such as a tuple, string, or set.

#method 
#con.append() # adds an item to the end of the list

#functions
#len("new") # returns the number of items in a list
#print(type(con)) # Output: <class 'list'>

tuple= ("emmanuel", "james", "sam", "daniel")
print(tuple)
"""
tuples are immutable sequences, typically used to store collections of heterogeneous data.
Tuples are created using parentheses ().

"""
#list 
mylist = ["emmanuel", 5.6, "male", True ]
print(mylist.append("new item")) # this method is available for lists because lists are mutable, meaning that their
# elements can be changed, added, or removed.


#tuple
mytuple = ("emmanuel", 5.11, "male", False) 
#append() # this method is not available for tuples because tuples are immutable, meaning that once they are 
# created, their elements cannot be changed, added, or removed.
mytuple
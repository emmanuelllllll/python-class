class User:
 # make a mock model for instagtam signup page
 first_name = "Emmanuel"
 last_name = "Chibuike"
 age = 20
 gender = "male"
 email = "blahblah@gmail.com"
 nationality = "Targarian"
 phone = "08123456789"

# class is a blueprint for creating objects in python it is a way to bundle data and functionality together.

user1 = User()
print(user1.first_name)
print(user1.last_name)
print(user1.age)
print(user1.gender)
print(user1.email) 
print(user1.nationality)
print(user1.phone)
 
# the __init__ () method
# the __init__ () method is a special method that is called when an object is instantiated. It is used to initialize the attributes of the object.


# the __init__ () method
# the __init__ () method is a special method that is called when an object is instantiated. It is used to initialize the attributes of the object.
class User:
    # firstname = "majesty"
    # lastname = "chibuikem"
    # age = 30
    # sex = "gay"
    # nationality = "ibiza"
    # email = "chichi@gmail.com"
    # phone = "77"

    # a constructor is a special method that is called when an object is instantiated. It is used to initialize the attributes of the object.
    def __init__(self,firstname, lastname, age, sex, nationality, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.nationality = nationality
        self.email = email
        self.phone = phone

 

user1 = User("majesty", "chibuikem", 30, "gay", "ibiza", "chichi@gmail.com", 7777)

# print(user1.firstname)
def first_name(self):
        print(self.firstname)


# print(user1.firstname)
# print(user1.lastname)
# print(user1.age)
# print(user1.sex)
# print(user1.nationality)
# print(user1.email)
# print(user1.phone)
 
# dog 
# make a constructor that will get the dogs name and breed 
# make a methond bark that will print woof woof
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")
dog = Dog("molly", "german shepherd")
print(dog.name)
print(dog.breed)
dog.bark()
print("woooooofffffffff")


class Cat:
    def __init__(self, name, breed ):
        self.name = name
        self.breed = breed

    def meow(self):
        print("meow meow ")
    
    def printName(self):
        print(self.name)
mycat = Cat ("kamal","tabby-cat")
print(mycat.name)
print(mycat.breed)

# make a new str method that will say this method returns your name and your breed
def __str__(self):
        return f"This class requires your name and your breed\nEmmanuel"

# create a human class it should have the 5 senses and thier name and skin color, limbs and height 
# class Human:
#     def __init__(self, name, skin_color, limbs, height):
#         self.name = name
#         self.skin_color = skin_color
#         self.limbs = limbs  
#         self.height = height

#     def senses(self):
#         print("sight, hearing, taste, touch, smell")

#     def printName(self):
#         print(self.name)

#     def printSkinColor(self):
#         print(self.skin_color)

#     def printLimbs(self):
#         print("hands and legs")   

#     def printHeight(self):
#         print(self.height)

#     # ✅ Add walk method inside class
#     def walk(self):
#         print("I am walking")

#     # ✅ Add talk method inside class
#     def talk(self):
#         print("I am talking")


# # Create an object
# human1 = Human("emmanuel", "brown", 4, "5.9ft")

# # Print attributes
# print(human1.name)
# print(human1.skin_color)
# print(human1.limbs) 
# print(human1.height)

# # Call methods
# human1.senses()
# human1.printName()
# human1.printSkinColor()
# human1.printLimbs()
# human1.printHeight()

# # ✅ Call new methods
# human1.walk()
# human1.talk()


"""
human class
constructor - name, five senses, limbs, skin tone, height
methods -walking, talking
"""

class Human:
    def __init__(self, name, eyes, ears, nose, tongue, skin, limbs, skinTone, height):
        self.name = name
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.tongue = tongue
        self.skin = skin
        self.limbs = limbs
        self.skinTone = skinTone
        self.height = height
    def walking(self):
        print(f"{self.name} am walking")
    def talking(self):
        print(f"{self.name} am talking")

Emmanuel= Human("EMMANUEL", 2,2, 1, 1,"feeling",4, "dark", "6.1ft")
print(Emmanuel.name)
print("two eyes", Emmanuel.eyes)
print("two ears", Emmanuel.ears)
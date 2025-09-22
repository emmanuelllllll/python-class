class Human:
    # Constructor - sets up the human
    def __init__(self, eyes, hair, legs, gender, height, mouth ):
        self.eyes = eyes
        self.hair = hair
        self.legs = legs
        self.gender = gender
        self.height = height
        self.mouth = mouth  # Local variable, not stored in the object

    # Actions the human can do
    def walk(self):
        print("I am walking...")

    def speak(self):
        print("I am speaking...")

    def breathe(self):
        print("I am breathing...")
    


# Create a human
person1 = Human(2, "black", 2, "male", "6ft", "big")

# Show details
print("Eyes:", person1.eyes)
print("Hair:", person1.hair)
print("Legs:", person1.legs)
print("Gender:", person1.gender)
print("Height:", person1.height)
print("Mouth:", person1.mouth)  # This will raise an AttributeError
# Call actions
person1.walk()
person1.speak()
person1.breathe()

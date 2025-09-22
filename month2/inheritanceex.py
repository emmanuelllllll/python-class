class person:
    def __init__(self, fname, lname):
        self.fname =fname
        self.lname =lname
    def printfullname(self):
        print(self.fname + "" + self.lname)


class student(person):
    def printlastname(self):
        print(self.lname)
me = person("emmanuel","chibuike")
me.printfullname()  
last = student("last", "chibike")
last.printlastname()
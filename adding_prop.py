class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation = year
    def Welcome(self):
        print("Welcome", self.firstname, self.lastname, " to the class of ", str(self.graduation))

x = Student("Mike", "Olsen", 2019)
x.Welcome()

mystr = "banana"
myit = iter(mystr)

for x in mystr:
    print(next(myit))

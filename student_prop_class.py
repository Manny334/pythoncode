class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
print("My name is " +x.firstname+" "+x.lastname+" and the graduation year is "+str(x.graduationyear))
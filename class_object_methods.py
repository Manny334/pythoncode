class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self): # 'self' parameter is a reference to the current instance of the class and is used to access variables that belong to the class
        print("Hello my name is: " + self.name)
p1 = Person("John", 36)
p1.myfunc()
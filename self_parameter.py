class Person:
    def __init__(input, name, age):
        input.name = name
        input.age = age
    def myfunc(input_1):
        print("Hello my name is " + input_1.name + " and my age is: " + str(input_1.age))
p1 = Person("John", 36)
del p1.age
p1.myfunc()
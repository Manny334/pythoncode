class Person:
    def __init__(self, name, age):  # '__init__() function is always executed ehrn the class is being inititated'
        self.name = name            # 'we can use __init__() function too assign values to object properties'
        self.age = age
p1 = Person("John", 36)

print(p1.name)
print(p1.age)
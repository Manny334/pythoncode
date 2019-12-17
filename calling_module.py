import mymodule
from mymodule import person1
mymodule.greeting("Manish")  # syntax for using a function from a module, use
                             # module_name.function_name

a = mymodule.person1["age"]
print(a)

print(person1["age"])

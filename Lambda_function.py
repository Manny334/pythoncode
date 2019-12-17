# A Lambda function is a small anonymous function
# Can have any number of arguments but can only have one expression
# syntax: lambda  arguments : expression
# use lambda function when an anonymous function is required for a short period of time
x = lambda a: a + 10
print(x(5))

y = lambda a, b: a * b
print(y(5, 6))

def myfunc(n):
    return lambda a: a * n # doubles the result by taking two values

my_doubler = myfunc(2)

print(my_doubler(11))

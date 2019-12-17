numbers = [1, 2, 3]
# creating an explict iterator
it = iter(numbers)
print(it.__next__()) # First way to do it
print(next(it)) # more convenient way
print(next(it))

fileIt = open('grades.txt')
print(next(fileIt), end='')

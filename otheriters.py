numbers = range(1, 11)
it = iter(numbers)
print(next(it))
import os
files = os.popen('dir *.py')
fileit = iter(files)
print(next(fileit))
for file in files:
    print(file)
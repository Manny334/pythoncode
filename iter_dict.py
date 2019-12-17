grades = {'Clayton': 100, 'Arthur': 150, 'John': 200}
#for key in grades.keys():
#   print(key, grades[key])
it = iter(grades)
print(next(it))
print(next(it))
for key in grades:
    print(key, grades[key])

file = open('grades.txt')
grades = file.readlines()
print(grades)
for i in range(len(grades)):
    grades[i] = grades[i].rstrip() # Here we are stripping the new line displayed using the rstrip function
print(grades)

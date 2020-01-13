# Write a python program to generate and print a list expet for the first 5
# elements, where the values are square of numbers between 1 & 30

def printValues():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l[5:])

printValues()
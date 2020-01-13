import re
txt = "The rain in Spain"
str = "The rain in India"
y = re.findall("[a-m]", str)
x = re.search("^The.*Spain$", txt)
if (x):
    print("We got a match")
else:
    print("No match")
print(y)
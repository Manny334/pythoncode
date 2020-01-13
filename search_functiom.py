import re

str = "The rain in Beauclair"

x = re.search("\s", str)

print("The first whitespace in string starts at position: ", x.start())
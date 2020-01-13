import re

str = "That would be 200 crowns!!! master!!"

x = re.findall("\d", str)

print(x)
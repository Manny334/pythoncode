# python does not have built-in support for arrays, but python lists can be used instead
cars = ["BMW", "Nissan", "Chevrolet"]
x = cars[0]
y = len(cars)
print(x)
print(y)

bikes = ["BMW", "Toyota", "Nissan"]

for x in bikes:
    print(x)

bikes.append("Honda")
print(bikes)


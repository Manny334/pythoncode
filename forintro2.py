sentence = "now is the time for all good people to come to the aid"
count = 0
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print("The number of vowels is " + str(count))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(numbers)):
    print(numbers[i])


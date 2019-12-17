numbers = (1, 2, 3, 4, 5)
sum = 0
for num in numbers:
    sum = sum + num
    print(num)
print("THe sum is " + str(sum))

words = ("now", "is", "time", "the")
for word in words:
    print(word)
max = 0
for i in range(1, len(words)):  # Here, we assume that the longest word is 'now'
    if len(words[i]) > len(words[max]):
        max = i
print("The longest word is " + words[max])

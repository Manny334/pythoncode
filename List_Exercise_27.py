# Write a python program to find the second smallest numbers in a list
def second_smallest(numbers):
    if(len(numbers)<2):
        return
    if((len(numbers) == 2) and (numbers[0] == numbers[1])):
        return
    dup_items = set()
    uniq_items = []
    for x in numbers:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    uniq_items.sort()
    return uniq_items[1]

print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2,2]))
print(second_smallest([2]))
# Write a python program to get unique values from a list

list_numbers = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original list: ", list_numbers)
my_set = set(list_numbers)
my_new_list = list(my_set)
print("List of unique numbers: ", my_new_list)
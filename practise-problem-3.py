# Python Practice 3 | Python Tutorials For Absolute Beginners In Hindi
# The task you have to perform is “Foods and Calories.” This task consists of a total of 15 points to evaluate your performance.

# Problem Statement:-
# You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

# You have to use the following three methods to reserve a list:

# Inbuild method of python
# List name [::-1] slicing trick
# Swapping the first element with the last one and second element with second last one and so on like,
# [6 7 8 34 5] -> [5 34 8 7 6]

# Input:
# Take a list as an input from the user

# [5, 4, 1]

# Output:
# [1, 4, 5]

# [1, 4, 5]

# [1, 4, 5]


# All three methods give the same results!

# The program starts from here!

ListIn = int(input("Please enter the size of the list:\n"))

ls = []

for i in range(ListIn):
    ls.append(int(input("Please enter the list element")))

print(f"Your list is:")
for i in ls:
    print(i)

print("We have reversed the list for you!")

ls = ls[::-1]
for i in ls:
    print(i)

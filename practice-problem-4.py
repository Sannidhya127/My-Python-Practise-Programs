# Python Problem 4
# The task you have to perform is “The Next Palindrome.” This task consists of a total of 15 points to evaluate your performance.
# Problem Statement: -
# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
# 676, 616, mom, 100001.
# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.
# Input:
# 3
# 451
# 10
# 2133
# Output:
# Next palindrome for 451 is 454
# Next palindrome for 10 is 11
# Next palindrome for 2311 is 2222


# *! Code starts from here


# ** The Next Palindrome **

import time


def PalindromeNum(num):
    while True:
        # num = num + 1
        num = str(int(num))
        if num == num[::-1]:
            print(f"{num} is already a Palindrome")
            # *! num = str(int(num) )
            # *! print(f"The next Palindrome is {num}")
            break
        else:
            num = str(int(num)+1)


if __name__ == "__main__":
    NumberOfTestCases = int(input(
        "Please enter the number of items you want to take out the palindrome of:\n"))
    for i in range(NumberOfTestCases):
        MainNum = input("Enter the number here:\n")
        PalindromeNum(MainNum)

    print("We are glad that you used our system. Do come back again!")
    time.sleep(4)

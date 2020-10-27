# Practice Problem 2 (Easy) | Python Tutorials For Absolute Beginners In Hindi
# The task you have to perform is “Divide the Apples.” This task consists of a total of 10 points to evaluate your performance.

# Problem Statement: -
# Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.

# You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

# Input:

# Take input n, mn, and mx from the user.

# Output:
# Print whether the numbers between mn and mx are divisor of “n” or not. If mn = mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

# Example:
# If n is 20 and mn = 2 and mx = 5

# 2 is a divisor of20

# 3 is not a divisor of 20

# …

# 5 is a divisor of 20
try:
    nTerm = int(
        input("Please enter the number whose divisor you wish to find out:\n"))

    mnTerm = int(input(
        "Please enter the first number in the range from where you want to start counting the divisor"))
    mxTerm = int(input(
        "Please enter the second number in the range from where you want to stop counting the divisor"))
    for i in range(mnTerm, mxTerm+1):
        divided = nTerm % i
        if mnTerm < mxTerm:
            if divided == 0:
                # print(nTerm / i)
                print(f"The number {i} is a divisor of the number {nTerm}")

            elif nTerm % i != 0:
                print(f"The number {i} is not a divisor of the number {nTerm}")


except ValueError:
    print(
        "Please don't enter any kind of punctuations ()!@#$%^&*}{:><>?][;l.,./ or alphabets ")

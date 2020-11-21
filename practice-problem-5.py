# *! Python Problem 5 | Python Tutorials For Absolute Beginners In Hindi #111
#  *! The task you have to perform is “Palindromify the List.” This task consists of a total of 10 points to evaluate your performance.

# *! The task is very similar to the previous one i.e. Tutorial #109 ( Pyhton Problem 4)

# *! Problem Statement:-
# *! You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10; otherwise, you will print that number.

# *! Input:
# *! [1, 6, 87, 43]

# *! Output:
# *! [1, 6, 88, 44]

#  *? Code starts from here


def Palinfromefier(PalindromeNum, listPal):
    while True:

        # if PalindromeNum >= 10:
        PalindromeNum = str(int(PalindromeNum))
        if PalindromeNum == PalindromeNum[::-1]:
            # print(f"Your palindrome is {PalindromeNum}")
            listPal.append(PalindromeNum)
            break
            # print("Thank You")

        else:
            PalindromeNum = str(int(PalindromeNum)+1)
            listPal.append(PalindromeNum)
        for i in listPal:
            print(i)


if __name__ == "__main__":
    NumOfCases = int(
        input("Please enter the number of items you will palindrofy:\n"))
    Palindromes = []
    for i in range(NumOfCases):
        num = int((input("Please enter the number here:\n")))
        # print("")
        Palinfromefier(num, Palindromes)

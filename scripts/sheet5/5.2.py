"""Definition: this module defines whether a number is palindromic and what the 
largest palindromic number derived from products of any 3 digit numbers
author: Lennart Elbe (lenni.elbe@gmail.com)

"""


def palindromic(n):  # number to string and then string is flippped
    """
    determines if given int n is a palindrome or not. 
    returns true if the palindrome is a palindrome
    returns false otherwise
    examples:
    >>> palindromic(9009)
    True
    >>> palindromic(101)
    True
    >>> palindromic(35)
    False
    """
    v = str(n)
    if v == v[-1::-1]:
        return True
    return False


print(palindromic(9009) == True)
print(palindromic(900) == False)


def max_palindrome():  # finds the maximum palindrome in a range from 100-999 (all three digit numbers)
    """
    this definition defines the maximum possible palindrome in all products of all three digit numbers 100-999.
    arguments: none
    returns: an integer, the maximum value in paliList, a list of the palindromes calculated
    example:
    N/A
    """
    paliList = []
    # these two for loops cover every posisble combination of three digit numbers
    for a in range(100, 1000):
        for b in range(100, 1000):
            if palindromic(a*b):
                # appends new palindrome and calls palindromic() function
                paliList.append(a*b)
    return max(paliList)


print(max_palindrome() == 906609)

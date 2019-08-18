#returns nth fibonacci value
"""
definition: this module defines the fibonacci number at nth place(NOT index) of fibonacci sequence.
author:Lennart Elbe(lenni.elbe@gmail.com)
"""


def fib(n):  # calculate fibonacci numbers up to input number
    """Author: Lennart Elbe (lenni.elbe@gmail.com)
    definition:This module calculates the fibonacci number at the nth place.
    arguments: n, the nth fibonacci number you want to find
    returns: element at nth index of list of fibonacci numbers
    example: 
    """
    fibList = [0, 1]
    for x in range(2, n+1):  # hits every value to n
        # calculates last two numbers together and adds them to list
        fibList.append(fibList[x-2] + fibList[x-1])
    return fibList[n]


print(fib(3))
print(fib(10))

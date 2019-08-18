"""
Problem 1: Homeprimes.py

Authors:
    Lennart Elbe <lenni.elbe@gmail.com>

.. _`Python Standard Library`:
    https://docs.python.org/3.7/library
"""


def primes(n):
    """Finds all prime numbers smaller than n.a

    args:
        n {int} -- The given integer.

    returns:
        list -- A list of all prime numbers smaller than n.
    """

    l = []
    for i in range(2, n+1):
        indivisible = True
        for x in l:
            if i % x == 0:
                indivisible = False
        if indivisible:
            l.append(i)
    return l


def primefactors(n):
    """takes in an int and returns all prime factors of that integer

    args:
        n {int} -- The number whose prime factors are found.

    returns:
        list -- The list of prime factors of n.
    """
    factors = []
    for i in primes(n):
        while n % i == 0:
            factors.append(i)
            n = n/i
    return factors


def homeprime(n):
    """Calculates the homeprime of a given integer.
    
    args:
        n {int} -- The given integer.
    
    returns:
        int -- The homeprime of n.
    """

    m = ''
    pfactors = primefactors(n)
    for i in pfactors:
        m += str(i)
    m = int(m)
    if len(pfactors) == 1:
        return m
    return homeprime(m)

print(homeprime(9) == 311)
print(homeprime(10) == 773)
print(homeprime(5) == 5)
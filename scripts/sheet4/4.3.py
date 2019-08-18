#!/usr/bin/env python3
#start with empty list, if 1 < target ammend 1 to list, if 2 < w, current number= 2, nextNumber = cn + 1, if nn%cn=0


def primes(n):
    l = []
    for i in range(2, n+1):
        # test if i is prime, if i is prime add to l
        # we can test if i is prime by testing if i is divisible by previous elements in l
        # text each element in l if i is divisible by it
        indivisible = True
        for x in l:
            #print("is %d divisible by %d?" % (i, x))
            if i % x == 0:
                indivisible = False
            #    print("yes")
            #else:
            #    print("no")
        if indivisible:
            # i is divisible by all elements in l
            l.append(i)
    print(l)
    return l
    print("-------------------")  # for readability


print(primes(1) == [])
print(primes(3) == [2, 3])
print(primes(20) == [2, 3, 5, 7, 11, 13, 17, 19])

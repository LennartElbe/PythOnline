"""
Problem 1: powerset.py

Authors:
    Lennart Elbe <lenni.elbe@gmail.com>

.. _`Python Standard Library`:
    https://docs.python.org/3.7/library
"""


def powerset(s):
    """Calculates the power set of a list using recursion.

    args:
        s {list} -- The list (user input).

    returns:
        list -- The power set of s.
    """

    if s == []:
        return [[]]
    ps = [s]
    for i in s:
        # i is a number in the list
        sublist = [j for j in s if j != i]
        pstmp = powerset(sublist)
        for j in pstmp:
            if not(j in ps):
                ps.append(j)
    return ps


def test_powerset():
    assert powerset([]) == [[]], "Error for empty powerset"
    assert powerset([1, 2]) == [[1, 2], [2], [], [1]], "Error"
    assert powerset([1, 2, 3]) == [[1, 2, 3], [2, 3],
                                   [3], [], [2], [1, 3], [1], [1, 2]]
    assert powerset([1, [2]]) == [[1, [2]], [[2]], [], [1]], "error"

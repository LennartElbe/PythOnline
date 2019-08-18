"""
Problem 2: flatten.py

Authors:
    Lennart Elbe <lenni.elbe@gmail.com>

.. _`Python Standard Library`:
    https://docs.python.org/3.7/library
"""


def flatten(ls):
    """Flattens a list.
    Recursive calls to flatten(rest) lead to processing of every element in
    entire list.
    Includes case for len(ls) = 0.
    Returns a new variable flatlist which means that the original ls list is
    not changed.

    args:
        ls {list} -- The list to be flattened.

    returns:
        list -- The flattened list.
    """

    # erstes Element
    if len(ls) == 0:
        return ls
    erstesElement = ls[0]
    rest = ls[1:]
    flattenedRest = flatten(rest)
    # check erstesElement
    if type(erstesElement) != list:
        flatlist = [erstesElement]
        for a in flattenedRest:
            flatlist.append(a)
        return flatlist
    flatlist = flatten(erstesElement)
    for a in flattenedRest:
        flatlist.append(a)
    return flatlist


def test_flatten():
    """
    Runs a variety of tests on flatten().
    First with print statements and bools and then with assert statements.
    """

    t = [1, 4]
    print(flatten(t) == [1, 4])  # worked
    a = [3, 4, [[5]]]
    b = [[[1, 2, a], (6, [7]), 8], 9, False]
    c = flatten(b)
    print(a == [3, 4, [[5]]])  # worked
    print(b == [[[1, 2, [3, 4, [[5]]]], (6, [7]), 8], 9, False])  # worked
    print(c == [1, 2, 3, 4, 5, (6, [7]), 8, 9, False])  # worked

    a = [3, 4, [[5]]]
    b = [[[1, 2, a], (6, [7]), 8], 9, False]
    c = flatten(b)
    assert flatten([]) == [], "Error"
    assert flatten([1]) == [1], "Error"
    assert a == [3, 4, [[5]]], "Error"
    assert b == [[[1, 2, [3, 4, [[5]]]], (6, [7]), 8], 9, False], "Error"
    assert c == [1, 2, 3, 4, 5, (6, [7]), 8, 9, False], "Error"


test_flatten()

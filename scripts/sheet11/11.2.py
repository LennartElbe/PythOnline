"""
Problem 1: crack_caesar.py
A class used to decode a caesar cypher and return the shift used originally.

Authors:
    Lennart Elbe <lenni.elbe@gmail.com>

.. _`Python Standard Library`:
    https://docs.python.org/3.7/library
"""
from caesar import caesar

frequency_english = {"e":   12.702,
                     "t":   9.056,
                     "a":   8.167,
                     "o":   7.507,
                     "i":   6.966,
                     "n":   6.749,
                     "s":   6.327,
                     "h":   6.094,
                     "r":   5.987,
                     "d":   4.253,
                     "l":   4.025,
                     "c":   2.782,
                     "u":   2.758,
                     "m":   2.406,
                     "w":   2.360,
                     "f":   2.228,
                     "g":   2.015,
                     "y":   1.974,
                     "p":   1.929,
                     "b":   1.492,
                     "v":   0.978,
                     "k":   0.772,
                     "j":   0.153,
                     "x":   0.150,
                     "q":   0.095,
                     "z":   0.074}


def compute_probability(input: str) -> dict:
    """takes every letter in the input and counts it, adds to dictionary,
    and calculates the frequencies thereof.

    Arguments:
        input {str} -- A given input, usually a sentence or series
        of sentences.

    Returns:
        dict -- A dictionary with key as letter and value as frequency
        of that letter in the input.
    """
    d = frequency_english.copy()
    for i in d:
        d[i] = 0
    for i in range(len(input)):
        if input[i] in d:
            d[input[i]] += 1
    sum = 0
    for i in d:
        sum += d[i]
    for i in d:
        d[i] = d[i]/sum*100
    return d


def compare_prob(d1: dict, d2: dict) -> float:
    """compares the frequency of letters in the sentence to
    the frequency of letters in the english language.

    Arguments:
        d1 {dict} -- The language dictionary (english).
        d2 {dict} -- The frequency of letters in the given input.

    Returns:
        float -- The chisquared outcome of the statistical comparison.
    """

    prob = 0
    for i in d2:
        prob += ((d1[i] - d2[i])**2)/d2[i]
    return prob


def crack_caesar(input: str) -> tuple:
    """Cracks the caesar cypher by computing the
    shift and probability of letters for every single possible shift.

    Arguments:
        input {str} -- [description]

    Returns:
        tuple -- [description]
    """

    t = ""
    minprob = None
    minshift = 0
    for shift in range(-13, 13):
        unshifted = caesar(input, shift)
        newdict = compute_probability(unshifted)
        prob = compare_prob(newdict, frequency_english)
        if minprob is None:
            minshift = shift
            minprob = prob
        else:
            if prob < minprob:
                minshift = shift
                minprob = prob
    return (caesar(input, minshift), minshift)


sentence = "far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the galaxy lies a small unregarded yellow sun"
x = caesar(sentence, 2)
print(x)
t, shift = crack_caesar(x)
print("t:" + t)
print("shift: %d" % shift)

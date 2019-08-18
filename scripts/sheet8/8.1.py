import pytest

LETTERS = ("abcdefghijklmnopqrstuvwxyz"
           "ABCDEFGHIJKLMNOPQRSTUVWXYZÃ„Ã–ÃœÃ¤Ã¶Ã¼ÃŸ")


def _next_word_helper(s):
    """Helper function for next_word.
    Recursive calls for [1:] (the rest of the string) ensure that
    the entire string is processed.

    args:
        s {str} -- The string to be read through to check for word breaks.

    returns:
        tuple -- Returns a tuple consisting of the first word and the rest of
        the input.
    """

    if not s:
        return None, s
    if s[0] not in LETTERS:
        return None, s
    word = s[0]
    word_rest, s_rest = _next_word_helper(s[1:])
    if word_rest:
        ############################################################
        # Semantic Error (second error):
        # By setting word equal to word_rest you lose the characters
        # that were in word.
        # That's why word_rest needs to be appended to word.
        ############################################################
        # word = word_rest
        word += word_rest
    return word, s_rest


def next_word(s):
    """Return the first word of an input string s and the rest of it.

    args:
        s {str} -- The user-inputted string.

    returns:
        tuple -- The first value of this tuple is the first word of the
        user-input and the second value is the rest of the word. None if there
        is only one word within the input.
    """

#    #################################################################
#    # Semantic error (third error):
#    # Prevents error during runtime if while loop tries to access
#    # character 0 of string (s[0]).
#    #################################################################
#    if len(s) == 0:
#        print("Length of string is 0")
#        return s, None

    ########################################################
    # Syntax error (first error and third error):
    #    Missing Colon after the definition of a while loop.
    #    Also check if the string is empty in each iteration.
    ########################################################
    # while s[0] not in LETTERS
    while (len(s) > 0) and (s[0] not in LETTERS):
        s = s[1:]
    return _next_word_helper(s)


# 8.1 (b)
def test_next_word():
    """Function for testing next_word().
    Uses assert to provide error messages.
    """
    # error test for short words
    assert next_word('') == (None, ''), "This is an error"
    assert next_word(' ') == (None, ''), " "
    # error test for keeping only last letter
    assert next_word('blue') == ('blue', '')
    assert next_word('ue') == ('ue', '')
    # error test for
    assert next_word('u') == ('u', '')
    assert next_word('bl ue') == ('bl', ' ue')


test_next_word()

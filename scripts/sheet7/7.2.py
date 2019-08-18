"""Tools for word trees.

Authors:
    Lennart Elbe {lenni.elbe@gmail.com}

Examples:
    

"""

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÃ„ÃœÃ–Ã¤Ã¼Ã¶ÃŸ"


def next_word(s):
    """Return the first word (or None) of an input string s and the rest of it.

    args:
        s: The input string.

    returns:
        Tuple containing the first word (str or None) and the rest of s (str).

    Examples:
    >>> next_word('asdf asdf xyqr')
    ('asdf', ' asdf xyqr')
    >>> next_word('echatsteinschalosch')
    ('echatsteinschalosch', '')
    >>> next_word('spam&&ham  ham...')
    ('spam', '&&ham  ham...')

    Leading whitespaces and other invalid characters are removed:
    >>> next_word(' &foo @bar')
    ('foo', ' @bar')

    If the input string contains no valid word, None is returned instead:
    >>> next_word('$$$')
    (None, '')
    >>> next_word('')
    (None, '')

    """
    skip = 0
    for c in s:
        if c in LETTERS:
            break
        else:
            skip += 1
    if skip == len(s):
        return None, ''

    take = 0
    for i in range(skip, len(s)):
        if s[i] in LETTERS:
            take += 1
        else:
            break

    return s[skip:skip + take], s[skip + take:]


class Node:
    """A node of a search tree.

    Attributes:
        mark (str): A word.
        frequency (int): The frequency with which the word (mark) occurs.
        left (tree): The left subtree.
        right (tree): The right subtree.
    """

    def __init__(self, mark, frequency, left, right):
        """Set attributes to their initial values.

        Args:
            mark (str): A word.
            frequency (int): The frequency with which the word (mark) occurs.
            left (tree): The left subtree.
            right (tree): The right subtree.
        """
        self.mark = mark
        self.frequency = frequency
        self.left = left
        self.right = right


def node_str(n):
    """Return a string representation of a search node.

    Args:
        n: A search tree node.

    returns:
        A string representing the search node.
    """
    if n is None:
        return repr(None)
    return "Node(" + repr(n.mark) + ", " + repr(n.frequency) + ", " + node_str(
        n.left) + ", " + node_str(n.right) + ")"


Node.__str__ = node_str


# wenn im Baum
#  dann entweder im Mark
#  oder im linken Baum
#  oder im rechten Baum


def word_in_tree(s, t):
    """Checks to see if a string is present in the tree. If present, returns
    True and location thereof. Otherwise, returns False and None.

    args:
        s {str} --  The word that is being searched for within the tree t.
        t {Node} --  The tree in which the word s is being searched for.

    returns:
        Bool --  True if the word is present in the tree, and false if not.
        Node --  The location at which the word is present.
    """

    # entweder an der aktuellen position
    if t is None:
        return (False, None)
    if t.mark == s:
        return (True, t)  # now we can do t.frequence++
    # oder im linken
    if t.left is not None:
        l, nl = word_in_tree(s, t.left)
        if l:
            return (l, nl)
    # oder im rechten Zweig
    if t.right is not None:
        r, nr = word_in_tree(s, t.right)
        if r:
            return (r, nr)
    # oder das wort ist nicht im Baum
    return (False, None)


def add_to_tree(s, t):
    """Adds a word to a tree at a None location.

    args:
        s {str} -- The word being added.
        t {Node} -- The tree the word is being added to.

    returns:
        Node -- The tree it was added to.
    """

    if t is None:
        t = Node(s, 1, None, None)
        return t
    if t.left is None:
        t.left = Node(s, 1, None, None)
        return t
    if t.right is None:
        t.right = Node(s, 1, None, None)
        return t
    t.right = add_to_tree(s, t.right)
    return t


# Ex. 7.2 (a)
def word_tree(s):
    """Creates a tree from the string of words given.

    args:
        s {str} -- The string of words given.

    returns:
        Node -- The tree created.
    """

    nextword, rest = next_word(s)
    tree = None
    while nextword is not None:
        # if nextword is already in the tree, make counter one larger
        isin, n = word_in_tree(nextword, tree)
        if isin:
            # word is already in tree
            n.frequency += 1
        else:
            tree = add_to_tree(nextword, tree)
        nextword, rest = next_word(rest)
    return tree


# Ex. 7.2 (b)
def word_freq(tree, word):
    """Finds the frequency of a given word in a given tree.

    args:
        tree {[type]} -- The given tree in which to search for the frequency
        of a word.
        word {[type]} -- The word whose frequency is to be searched for.

    returns:
        int -- The frequency of the given word.
    """

    isin, n = word_in_tree(word, tree)
    if not isin:
        return 0
    return n.frequency


# Ex. 7.2 (c)
def print_tree(tree):
    """The tree to be printed in a readable mannar.

    args:
        tree {[type]} -- The given tree to be printed.
    """

    if tree is None:
        return
    print("%s: %d" % (tree.mark, tree.frequency))
    print_tree(tree.right)
    print_tree(tree.left)

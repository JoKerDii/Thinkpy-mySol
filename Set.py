"""
def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res
"""

def subtract(d1, d2):
    """set subtraction is available as a method called difference or as an operator"""
    return set(d1) - set(d2)


"""
def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False
"""

def has_duplicates(t):
    """An element can only appear in a set once, so if an element in t appears more than once, 
    the set will be smaller than t. If there are no duplicates, the set will be the same size as t."""
    return len(set(t)) < len(t)

"""
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

"""
def uses_only(word, available):
    """checks whether all letters in are in available."""
    return set(word) <= set(available)



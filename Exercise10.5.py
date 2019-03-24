def is_sorted(t):
    """Checks whether a list is sorted.

    t: list
    returns: boolean
    """
    return t == sorted(t)

# test
# print(is_sorted([1, 2, 2]))
# print(is_sorted(['b', 'a']))

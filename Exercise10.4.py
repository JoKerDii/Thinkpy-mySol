def chop(t):
    """Removes the first and last elements of t.

    t: list
    returns: None
    """
    del t[0]
    del t[-1]

# test 
# t = [1, 2, 3, 4]
# chop(t)
# print(t)
    
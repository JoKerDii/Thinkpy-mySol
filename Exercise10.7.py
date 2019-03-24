def has_duplicates(mylist):
    """takes a list and returns True if there is
    any element that appears more than once."""
    for i in mylist:  
        if mylist.count(i) > 1:
            return True
    return False

# test
# print(has_duplicates(['a','b','c','d','e']))
# print(has_duplicates(['a','a','c','d','e']))


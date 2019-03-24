def nested_sum(t):
    """Takes a list of lists of integers and computes the total of all numbers in a list of lists.
   
    t: list of list of numbers
    returns: number
    """
    total = 0
    for nested in t:
        total += sum(nested)
    return total

# test
# t = [[1, 2], [3], [4, 5, 6]]
# nested_sum(t)
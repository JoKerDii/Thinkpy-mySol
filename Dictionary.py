def histogram(s):
    """Show the frequency of each letter appears in word s"""

    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

# test
d = histogram('Hello World')
print(d)

"""Dictionaries have a method called get 
that takes a key and a default value"""
print(d.get('o',0))
print(d.get('b',0))

def print_hist(h): 
    """prints each key and the corresponding value"""

    for c in h:
        print(c, h[c])

# test
h = histogram('parrot')
print_hist(h)

for key in sorted(h):
    """To traverse the keys in sorted order"""

    print(key, h[key])

def reverse_lookup(d, v):
    """This function takes a value and 
    returns the first key that maps to that value:"""

    for k in d:
        if d[k] == v:
            return k
    """If we get to the end of the loop, that means v doesn’t appear in the dictionary as a
    value, so we raise an exception."""
    raise LookupError()

# test
# h = histogram('parrot')
# k = reverse_lookup(h, 2)
# print(k)
# k = reverse_lookup(h, 3)
# print(k)


def invert_dict(d):
    """create a dictionary that maps from frequencies to letters"""
    
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            # list can appear as values in a dictionary
            inverse[val].append(key) 
    return inverse

# test

hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)


known = {0:0, 1:1}
def fibonacci(n):
    """“memoized” version of fibonacci"""   
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print(fibonacci(3))

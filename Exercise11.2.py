"""Read the documentation of the dictionary method setdefault 
and use it to write amore concise version of invert_dict."""

def invert_dict(d):
    """Inverts a dictionary"""
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key],[]).append(key)
    return inverse

if __name__ == '__main__':
    d = dict(a = 1, b = 2, c = 3, z = 1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val,keys)




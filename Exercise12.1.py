
def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    # dict.items() returns keys and values
    # here keys and values flipped over 
    # store pairs of letter and counts as tuples into a list
    for x, freq in hist.items():
        t.append((freq, x))
    # decreasing order
    # due to tuples in list, sort of list just according to the first element of tuples. 
    t.sort(reverse=True) 

    res = []
    for freq, x in t:
        res.append(x) # just store the letters

    return res
    

def make_histogram(s):
    """Make a map from letters to number of times they appear in s.
    A method to count the frequency of letters in a word and store in a dictionary

    s: string
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


if __name__ == '__main__':
    string = read_file('emma.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)


"""Note

Dict.get(key, default=None)
This method returns the value for the given key, if present in the dictionary. 
If not, then it will return None (if get() is used with only one argument)."""



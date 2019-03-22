def is_abecedarian(word):
    """returns True if the letters in a word appear in alphabetical order 
    (double letters are okay)."""

    mylist = []
    for i in word:
        mylist.append(ord(i))
    # .sort() dosen't return any value while sorted() does
    newlist = sorted(mylist) 
    for i in range(len(mylist)):
        if mylist[i] != newlist[i]:
            return False
    return True

# test

# ans1 = is_abecedarian("abceefg")
# ans2 = is_abecedarian("abcdefg")
# ans3 = is_abecedarian("abcedfg")
# print(ans1)
# print(ans2)
# print(ans3)

"""
# other solutions on book

# For is_abecedarian we have to compare adjacent letters, 
# which is a little tricky with a for loop:
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

# An alternative is to use recursion:
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

# Another option is to use a while loop:
def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True






"""
from string import punctuation, whitespace

# any book.txt
book = 'words.txt'

with open(book, 'r') as fd:
    words = fd.read().split()

#remove punctuation, whitespace, uppercase
def clean(word):
    """skip punctuation and whitspace"""
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
print ("{} has {} 'words'".format(book, len([clean(word) for word in words])))
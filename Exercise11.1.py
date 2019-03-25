"""Write a function that reads the words in words.txt and stores them as keys in a dictionary.
It doesn’t matter what the values are. Then you can use the in operator as a fast way
 to check whether a string is in the dictionary."""

def dictionary():
    """store the words in words.txt in a dictionary as keys"""

    with open('words.txt') as fin:
        wordlist = fin.read().splitlines()
    result = dict()
    for word in wordlist:
        result[word] = 1
    return result

print(dictionary())

"""
import uuid
# uuid.uuid4() generats unique IDs

def dictionary():

    with open('words.txt') as fin:
        wordlist = fin.read().splitlines()
    result = dict()
    for word in wordlist:
        result[word] = uuid.uuid4()
    return result

print(dictionary())

"""

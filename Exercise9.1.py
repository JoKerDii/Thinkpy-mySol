"""Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace)."""

def twentychar():
    """This function prints only the words with more than 20 characters"""

    fin = open('words.txt')
    for line in fin:
        word = line.strip() # delete the space before and behind the word
        if len(word) > 20:
            print (line + '\n')

# test
# twentychar()

def twentychar2():
    """Alternative function to print only the words with more than 20 characters"""
    with open('words.txt','r') as fd:
        wordList = fd.read().split() # split the word from space 
    print ([word for word in wordList if len(word) > 20])

# test
# twentychar2()
def avoids(word, strletter):
    """takes a word and a string of forbidden letters,
    and that returns True if the word doesn’t use any of the forbidden letters."""
    
    for letter in strletter:
        for wordletter in word:
            if wordletter == letter:
                return False       
    return True

# test
# sol1 = avoids('Hello',['o','a','e'])
# print(sol1)

# sol2 = avoids('hello','oae')
# print(sol2)


def avoids2():
    strletter = input("Please input a list of forbidden letters")
    fin = open('words.txt')
    wordList = fin.read().split()

    answers = [word for word in wordList \
        for letter in strletter \
            for wordletter in word \
                if wordletter != letter]

    print(len(answers))

# test
# avoids2()

import random 
def avoids3():
    """To find a combination of five forbidden letters 
    that excludes the smallest number of words

    I have no idea how to do it better
    Is there any easier way to find accurate answer?"""

    fin = open('words.txt')
    wordList = fin.read().split()

    for i in range(100):
        alphabet = ['a','b','c','d','e','f','g','h','i','j',\
        'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        sample = random.sample(alphabet, 5)

        sampleList = []
        result = []
        answers = [word for word in wordList \
            for letter in sample \
                for wordletter in word \
                    if wordletter != letter]
        sampleList.append(sample)
        result.append(len(answers))

    smallest = sampleList[result.index(max(result))]
    print(smallest)

avoids3()






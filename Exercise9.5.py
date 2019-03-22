
def uses_all(word, string):
    """This function takes a word and a string of required letters,
    and that returns True if the word uses all the required letters at least once."""
    for i in string:
        if i not in word:
            return False
    return True

def uses_all2(string):
    fin = open('words.txt')
    wordList = fin.read().split()
    answers = []
    for word in wordList:
        if uses_all(word,string) == True:
            answers.append(word)
    print(answers)
    return answers

# test

# uses_all2("aeiou")
# uses_all2("aeiouy")

# print(len(uses_all2("aeiou")))
# print(len(uses_all2("aeiouy")))


    
                


def has_no_e(word):
    hasno = True
    for i in range(len(word)):
        if word[i] == 'e':
            return False
    return True

# test
# has = has_no_e("hello")
# print(has)
        
def has_no_e2():
    """print only the words that have no “e” 
    and compute the percentage of the words in the list that have no “e”"""
    
    fin = open('words.txt','r')
    wordList = fin.read().split()
    truelist = [word for word in wordList if has_no_e(word) == True]
    # lentruelist = len(truelist)
    # lenalllist = len([word for word in wordList])
    percentage = str(len(truelist) / len([word for word in wordList])) 
    print ([word for word in wordList if has_no_e(word) == True])
    print ("The percentage of the words in the list that have no 'e':" + percentage)

# test
# has_no_e2()



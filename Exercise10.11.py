"""One solution with in operation"""
def reverse_pair():
    fin = open('words.txt')
    wordList = []
    for line in fin:
        word = line.strip()
        wordList.append(word)
    
    reversePair = []
    for i in wordList:
        if i[::-1] in wordList:
            reversePair.append(i)
    return reversePair

# test
# reverse_pair()


"""Binary selection"""
import bisect


def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word

def reverse_pair_bi(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if reverse_pair_bi(word_list, word):
            print(word, word[::-1])






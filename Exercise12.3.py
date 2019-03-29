def signature(s):
    """Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    t = list(s)
    t.sort() # t = sorted(t)
    t = ''.join(t)
    return t

def all_anagrams(filename):
    """Finds all anagrams in a list of words.
    filename: string filename of the word list
    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # sort and extract unique ones
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

def metathesis_pairs(d):
    """Print all pairs of words that differ by swapping two letters.

    d: map from word to list of anagrams
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    """Computes the number of differences between two words.

    word1, word2: strings
    Returns: integer
    """
    # two words are of the same length
    assert len(word1) == len(word2) 

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    # firstly find the anagrams, then it is easier to find two words with two different letters
    sets = all_anagrams('words.txt')
    metathesis_pairs(sets)
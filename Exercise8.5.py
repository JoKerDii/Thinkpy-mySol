def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    input:
    letter: single-letter string
    n: int
    
    output:
    single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    # in case that (c+n) is larger than 26, 
    # if so, the result of rotate should not exceed the alphabet range, 
    # instead, it should count to the end and restart from the first alphabet for the remaining n
    i = (c + n) % 26 + start 
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.
    input:
    word: string
    n: integer
    output:string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))
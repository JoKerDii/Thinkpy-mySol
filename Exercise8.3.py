def is_palindrome(word):
    """Returns True if word is a palindrome.
    One line version
    """
    if word == word[::-1]:
        return True
    else:
        return False

# test
# print(is_palindrome("ollo"))
# print(is_palindrome("hello"))

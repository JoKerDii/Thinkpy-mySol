def uses_only(word, strletter):
    """takes a word and a string of letters, and that
    returns True if the word contains only letters in the list."""
    
    for i in word:
        if i ==' ':
            continue
        elif i not in strletter:
            return False
        
    return True

# test
# sol = uses_only('Hoe alfalfa','acefhlo')
# print(sol)


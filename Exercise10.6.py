def is_anagram(string1, string2):
    """Te check whether two words are anagrams 
    Two words are anagrams if one can be rearranged the letters to spell the other."""
    return sorted(string1) == sorted(string2)

# test
# string1 = 'boots'
# string2 = 'boost'
# ans = is_anagram(string1,string2)
# print(ans)
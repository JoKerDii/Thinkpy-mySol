"""The following functions are all intended to check whether a string contains any lowercase
letters, but at least some of them are wrong. For each function, describe what the
function actually does (assuming that the parameter is a string)."""

def any_lowercase1(s):
    """If there is at least one lower case, return True, 
    elif the case are all upper cases, return False"""
    for c in s:
        if c.islower():
            return True
    else:
        return False
# test
# print(any_lowercase1('Hello'))

def any_lowercase2(s):
    """The answer is always 'True', because string 'c' is a lower letter """
    for c in s:
        if 'c'.islower():
            return 'True'
    else:
        return 'False'
# test
# print(any_lowercase2('HELLO'))

def any_lowercase3(s):
    """Only check the first case whether it is a lower letter,
    'return' stops the for loop"""
    for c in s:
        flag = c.islower()
        return flag

# test
# print(any_lowercase3("hELLO"))
# print(any_lowercase3("Hello"))

def any_lowercase4(s):
    """If the first letter is upper case, it is False. elif the first letter is lower case, it is True.
    While there are multiple letters, if there is at least a lower letter follows the upper letter, it is True.
    if there is at least two upper letters follows the lower letter, it is False"""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# test
# print(any_lowercase4("h")) # False or True is True
# print(any_lowercase4("H")) # False or False is False
# print(any_lowercase4("Hello")) # True or True is True


def any_lowercase5(s):
    """If there is at least a upper letter, return False, if always lower cases, return true"""
    for c in s:
        if not c.islower(): # to check all if it is upper
            return False
    return True
# test
# print(any_lowercase4("HELLO"))
# print(any_lowercase4("He"))




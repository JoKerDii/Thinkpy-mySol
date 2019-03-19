def check_fermat(a, b, c, n):
    """
    This function checks to see if Fermat’s theorem holds
    """
    if n > 2 and (a**n + b**n == c**n):
        print ("Holy smokes, Fermat was wrong!")
    else:
        print ("No, that doesn’t work.")

# test
# check_fermat(2,2,2,3)

def check_numbers():
    """
    This function checks whether the input numbers violate Fermat’s theorem
    """
    a = int(input("Please input a number for a: "))
    b = int(input("Please input a number for b: "))
    c = int(input("Please input a number for c: "))
    n = int(input("Please input a number for n: "))
    return check_fermat(a, b, c, n)

# test
# check_numbers()



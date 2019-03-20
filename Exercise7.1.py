import math


def mysqrt(a):
    """Calculates square root using Newton's method:
    a - positive integer < 0;
    x - estimated value, in this case a/2
    """
    x = a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
            break
        x = y

def test_square_root(list_of_a):
    """Displays outcomes of calculating square root of a using different methods;
    list_of_a - list of positive digit.
    """
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"
    
    line2a = "-"
    line2b = "---------"
    line2c = "------------"
    line2d = "----"
    
    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""
    
    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)
    
    for a in list_of_a:
        col1 = float(a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))

        print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)

test_square_root(range(1,10))
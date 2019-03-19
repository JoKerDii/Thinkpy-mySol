def is_triangle(a, b, c):
    """
    This function aims to check if it is possible to form a triangle from sticks with the given lengths
    """
    if a > (b+c) and b > (a+c) and c > (b+a):
        print("Yes.")
    elif a == b+c or b == a+c or c == a+b:
        print("Degenerate.")
    else:
        print("No.")

# test
# is_triangle(1,2,3)

def is_inputTriangle():
    """
    This function prompts the user to input three stick lengths 
    and check whether sticks with the given lengths can form a triangle.
    
    """
    a = int(input("Please input a number for a:"))
    b = int(input("Please input a number for b:"))
    c = int(input("Please input a numebr for c:"))
    is_triangle(a, b, c)

# test
# is_inputTriangle()





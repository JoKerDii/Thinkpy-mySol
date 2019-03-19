def recurse(n, s):
    """
    Output: s + (1+2+ ... + n)
    
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        
recurse(3, 0)

"""
Draw a stack diagram that shows the state of the program when it prints the result.

n = 3, s = 0
n = 2, s = 3
n = 1, s = 5
n = 0, s = 6

"""

# recurse(-1,0) 
"""
This application will not get a result

"""


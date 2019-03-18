"""
1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a value,
and calls the function twice, passing the value as an argument.
3. Copy the definition of print_twice from earlier in this chapter to your script.
4. Use the modified version of do_twice to call print_twice twice, passing 'spam'
as an argument.
5. Define a new function called do_four that takes a function object and a value and
calls the function four times, passing the value as a parameter. There should be
only two statements in the body of this function, not four.
"""
def print_spam():
    """
    print "spam"
    """
    print('spam')
    
def do_twice(f):
    """
    run the function twice
    """
    f()
    f()

# test
# do_twice(print_spam)

def print_twice(arg):
    """
    print the arg twice
    """
    print(arg)
    print(arg)

def do_twice(f, n):
    """
    run the function twice with the argument n
    """
    f(n)
    
# test
# do_twice(print_twice, "spam")

def do_four(f,n):
    do_twice(f, n)
    do_twice(f, n)
    
    
# test
# do_four(print_twice,"spam")
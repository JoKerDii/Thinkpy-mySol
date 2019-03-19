def Koch(t, length):
    """
    This function uses the turtle to draw a Koch curve with the given length
    """
    if length < 3:
        t.fd(length)
        return

    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)
    t.rt(120)
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)


def snowflake(t, n):
    """
    This function draws three Koch curves to make the outline of a snowflake.
    (a triangle with a Koch curve for each side).
    """
    for i in range(3):
        Koch(t, n)
        t.rt(120)

# test

# import turtle
# bob = turtle.Turtle()

# bob.pu()
# bob.goto(-150, 90)
# bob.pd()

# snowflake(bob, 300)



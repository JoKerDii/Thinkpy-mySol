def draw(t, length, n):
    """Draw a tree

    The branch length depends on both length arg and n arg (length*n)
    The number of node is n

    """
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    # recursion begins from "n-1" because the tree becomes binary from "n-1"
    # this is the left part from the "n-1" because the "draw" function follows the "turr left" command
    draw(t, length, n-1)
    # turn twice of the angle of right to make sure the symmetry, because the point has turned left for an angle
    t.rt(2*angle) 
    # this is the right part from the "n-1" because the "draw" function follows the "turn right" command
    draw(t, length, n-1)
    # every recursion turn an angle to the original direction and go back to the node
    t.lt(angle)
    t.bk(length*n)

# test
# import turtle
# bob = turtle.Turtle()
# draw(bob, 10, 5)

"""
1. Write a function called square that takes a parameter named t, which is a turtle.
It should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the
program again.
"""

import math
import turtle

# bob = turtle.Turtle()
# print(bob)
# turtle.mainloop()

def square(t):
    """
    t: turtle
    """
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
"""
2. Add another parameter, named length, to square. Modify the body so length of
the sides is length, and then modify the function call to provide a second argument.
Run the program again. Test your program with a range of values for
length.
"""

def square2(t, l):
    """
    t: turtle
    l: step length
    """
    for i in range(4):
        t.fd(l)
        t.lt(90)

"""
3. Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon.
Hint: The exterior angles of an n-sided regular polygon are 360/n degrees
"""

def polygon(t, l, n):
    """
    t: turtle
    l: step length
    n: sides
    """
    for i in range(4):
        t.fd(l)
        t.lt(360/n)
        
"""
4. Write a function called circle that takes a turtle, t, and radius, r, as parameters
and that draws an approximate circle by calling polygon with an appropriate
length and number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
"""
     
def polyline(t, n, l, a):
    """
    t: turtle
    n: sides
    l: step length
    a: angle
    """
    for i in range(n):
        t.fd(l)
        t.lt(a)
        
def arc(t,r):
    """
    t: turtle
    r = radius
    """
    arc_length = 2 * math.pi * r 
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = 360.0 / n
    
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    
    print("arc, step_length"+str(step_length) +", step_angle "+ str(step_angle) +", n =" + str(n))

def circle(t,r):
    """
    t: Turtle
    r: radius
    """
    arc(t,r)
	
"""
# alternative:

def circle(t, r):
	C = 2 * math.pi * r
	n = 360
	l = C / n
	polygon(t, l, n)
	
def general_circle(t,r,a):
	C = 2 * math.pi * r * abs(angle) / 360
	n = 360
	l = C / n
	step_angle = a/n
	polyline(t, n, l, step_angle)
	
def circle(t, r):
	arc(t, r, 360)
	
"""
    
"""
5. Make a more general version of circle called arc that takes an additional
parameter angle, which determines what fraction of a circle to draw. angle is in
units of degrees, so when angle=360, arc should draw a complete circle.
"""
def general_arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

    print("arc, step_length"+str(step_length) +", step_angle "+ str(step_angle) +", n =" + str(n))

def general_circle(t,r):
    """
    t: Turtle
    r: radius
    """
    general_arc(t, r, 360)
    
    
# Test

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # wait for the user to close the window
    turtle.mainloop()
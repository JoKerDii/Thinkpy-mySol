def gcd(a,b):
    """ The solution of greatest common divisor (GCD)"""

    if b == 0:
        return a
    else:
        return gcd(b, a % b)



        
        
def displacement (Vinitial, t, a):
    """Compute the displacement of an object.

    Vinitial -- intial velocity of object
    t -- change in time
    a -- acceleration of object
    """

    return Vinitial*t + 0.5*a*t**2

#code below does not work properly yet
def quadratic (b,a,c):
    import math
    return b*math.sqrt(b**2-4*a*c)/2

def absolute(x):
    """determine the absolute value of a number."""
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0
def percentDifference(accepted, measured):
    """Determine the percent difference between an accepted value and a measured
        value. Both values must have the same units."""

    return absolute(measured-accepted)/accepted*100

def Heron(x,g):
    """Determine the square root of a given number."""
    accuracy = 0.001
    while absolute(g**2-x)>= accuracy:
        g=(g+x/g)/2
    return (round(g,3))

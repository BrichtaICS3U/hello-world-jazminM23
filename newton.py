def absolute(x):
    """determine the absolute value of a number."""
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0

#code below does not work
def newtonMethod(x,g):
    """Find the square root of a given number."""
    accuracy=0.001
    while absolute(g**2-x)>= accuracy:
        g= g-(g**2-x)/(2*g)
    return (round(g,3))

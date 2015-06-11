# 6.00 Problem Set 2
# Name: Andrew Marton
# Successive Approximation
# Time: ~70m

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    order = len(poly) - 1
    fofx = 0.0
    for n in range(order, -1, -1):
        fofx += x ** n * poly[n]
    return fofx

#print(evaluate_poly((1.0, 0.0, 5.0, 9.3, 7.0), -13.0))

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    order = len(poly) - 1
    derivlist = []
    if order == 0:
        return (0.0,)
    else:
        for n in range(1, order + 1, 1):
            derivlist.append(n * poly[n])
        return tuple(derivlist)

#print(compute_deriv((-13.39, 0.0, 17.5, 3.0, 1.0)))

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    i = 0
    fofx = epsilon + 1.0
    while abs(fofx) > epsilon:
        fofx = evaluate_poly(poly, x_0)
        fprimeofx = evaluate_poly(compute_deriv(poly), x_0)
        x_0 = x_0 - fofx / fprimeofx
        i += 1
    return (x_0, i)

print(compute_root((-13.39, 0.0, 17.5, 3.0, 1.0), 0.1, 0.0001))

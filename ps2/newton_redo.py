def evaluate_poly(poly, x):
    '''
    Takes a polynomial function (as tuple) and a number (float) and calculates value.
    Tuple indices correspond to order of coefficient, eg. 2x^2 + 4x + 3 -> (3, 4, 2)
    '''
    n = 0
    y = 0
    for c in poly:
        y += c * x ** n
        n = n + 1
    return y

test = (2, 2, 3, 1.5)
#print(evaluate_poly(test, 3))

def compute_deriv(poly):
    '''
    Computes the derivative of a polynomial in tuple form. If deriv is 0, returns
    tuple (0.0,)
    '''
    n = 1
    plist = []
    if len(poly) > 1:
        for c in poly[1:]:
            plist.append(c * n)
            n = n + 1
    else:
        plist = [0,]
    return tuple(plist)

#print(compute_deriv(test))

def compute_root(poly, x0, eps):
    '''
    Uses Newton's method to find and return a root of some polynomial function.
    Returns a tuple containing the root and number of iterations to achieve.
    '''
    for n in range(1000):
        if abs(evaluate_poly(poly, x0)) > eps:
            xn = x0 - evaluate_poly(poly, x0)/evaluate_poly(compute_deriv(poly), x0)
            x0 = xn
        else:
            output = (xn, n)
            break
    return output

print(compute_root(test, 10, 0.01))

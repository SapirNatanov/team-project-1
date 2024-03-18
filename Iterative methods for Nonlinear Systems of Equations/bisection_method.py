'''
Date: 18/3/2024
Group: Sapir Natanov 322378068
Dor Maudi 207055138
Noa Yasharzadeh 208595157
Segev Isaac 207938085
Group Git: https://github.com/DorMaudi/team-project-1
Name: Sapir Natanov 322378068
'''
import math
import numpy as np
from colors import bcolors
import sympy as sp

"""
Receives 3 parameters:
    1.  a - start value.
    2.  b - end  value. 
    3.  err - value of tolerable error

Returns variables:
    1.  S - The minimum number of iterations required to reach the desired accuracy
"""
def max_steps(a, b, err):
    s = int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))
    return s


"""
Performs Iterative methods for Nonlinear Systems of Equations to determine the roots of the given function f
Receives 4 parameters:
    1. f - continuous function on the interval [a, b], where f (a) and f (b) have opposite signs.
    2. a - start value.
    3. b - end  value. 
    4. tol - the tolerable error , the default value will set as 1e-16

Returns variables:
    1.  c - The approximate root of the function f
"""


def bisection_method(f, a, b, tol=1e-6):
    f_tag = sp.diff(f)
    f = sp.lambdify(x,f)
    originalFunc = f
    f_tag_flag = False

    if np.sign(f(a)) == np.sign(f(b)):
        tag = sp.lambdify(x, f_tag)
        if np.sign(tag(a)) == np.sign(tag(b)):
            raise ValueError("The scalars a and b do not bound a root")
        else:
            f = tag
            f_tag_flag = True

    c, k = 0, 0
    steps = max_steps(a, b, tol)  # calculate the max steps possible

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))

    # while the diff af a&b is not smaller than tol, and k is not greater than the max possible steps
    while abs(b - a) > tol and k < steps:
        c = a + (b - a) / 2  # Calculation of the middle value

        if f(c) == 0:
            return c  # Procedure completed successfully

        if f(c) * f(a) < 0:  # if sign changed between steps
            b = c  # move forward
        else:
            a = c  # move backward

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(k, a, b, f(a), f(b), c, f(c)))

        k += 1

    if f_tag_flag:
        if abs(originalFunc(c)) > tol:
            raise ValueError("The scalars a and b do not bound a root")

    if sp.floor(f(c)) != 0:
        raise ValueError("No solution found")

    return c


if __name__ == '__main__':
    x = sp.symbols('x')
    f = (6 * x**3 + x**2 + 2)/(2 * x - 6)
    a, b = -3, 0
    nextTest = (b - a) / 1000
    i = a + nextTest

    while i <= b:
        try:
            roots = bisection_method(f, a, i)
            print(bcolors.OKBLUE, f"\nThe equation f(x) has an approximate root at x = {roots}", bcolors.ENDC, "\n")
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        a = i
        i += nextTest
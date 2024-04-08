import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from colors import bcolors
from sympy.utilities.lambdify import lambdify

x = sp.symbols('x')


def simpsons_rule(f, a, b, n):
    """
    Simpson's Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of sub intervals (must be even).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    if n % 2 != 0:
        raise ValueError("Number of sub intervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n

    integral = f(a) + f(b)  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3

    return round(integral, 5)


if __name__ == '__main__':
    f = lambda x:(math.cos(x) + (x**3 - x + 2))/(2 * math.e ** (-x + 2))
    n = 60
    a = -3.1
    b = -1.4

    print(f" Division into n = {n} sections ")
    integral = simpsons_rule(f, a, b, n)
    print(bcolors.OKBLUE, f"Numerical Integration of definite integral in range [{a}, {b}] is {integral}", bcolors.ENDC)

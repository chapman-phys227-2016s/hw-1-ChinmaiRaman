#! /usr/bin/env python

"""
File: centered_diff.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 1.3
Date: Feb 12, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Function for numberical differentiation and errors in approximation
"""

import numpy as np

def diff(f, x, h = 1e-5):
    """
    Approximates the derivative of a function at a given value of x.
    """
    return ((f(x + h) - f(x - h)) / (2.0 * h))

def test_diff():
    """
    Tests the diff function above.
    """
    f = lambda x: float(x**2)
    assert(abs(diff(f, 3) - 6.0) < 1e-10), "Failure."
    
def application():
    """
    Prints the errors of the approximations of the derivatives of given functions.
    """
    ex = lambda x: np.exp(x)
    ex2 = lambda x: np.exp(-2.0 * (x**2))
    cos = lambda x: np.cos(x)
    ln = lambda x: np.log(x)
    
    print("f(x)\t\tx\tf'(x)\tapproximation of f'(x)\terror")
    print("e^x\t\t0\t1\t" + str(diff(ex, 0, 0.01)) + "\t\t" + str(abs(diff(ex, 0, 0.01) - 1)))
    print("e^(-2x^2)\t0\t0\t" + str(diff(ex2, 0, 0.01)) + "\t\t\t" + str(abs(diff(ex2, 0, 0.01) - 0)))
    print("cos(x)\t\t2pi\t0\t" + str(diff(cos, 2 * np.pi, 0.01)) + "\t\t\t" + str(abs(diff(cos, 2 * np.pi, 0.01) - 0)))
    print("ln(x)\t\t1\t1\t" + str(diff(ln, 1, 0.01)) + "\t\t" + str(abs(diff(ln, 1, 0.01) - 1)))
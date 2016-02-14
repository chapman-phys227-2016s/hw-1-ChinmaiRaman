#! /usr/bin/env python

"""
File: adaptive_trapezint.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 1.1
Date: Feb 12, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Uses Trapezoid Rule to find the integral of a function within a given error margin,
and outputs the number of trapezoids used.
"""
import numpy as np

def sec_dev(f, x, h=1e-6):
    """
    Calculates the second derivative of a function at a given x, given a small h
    """
    return (f(x - h) - 2 * f(x) + f(x + h)) / float(h**2)

def sec_dev_max(f, a, b):
    """
    Calculates the max second derivative within the range [a,b]
    """
    n = 999999
    i = (b - a) / float(n)
    max = abs(sec_dev(f, a))
    for counter in range(n):
        temp = abs(sec_dev(f, a + (counter + 1) * i))
        if temp > max:
            max = temp
    return max

def adaptive_trapezint(f, a, b, eps=1e-5):
    """
    Uses Trapezoid Rule to find the integral of a function within a given error margin,
    and outputs the number of trapezoids used.
    """
    # h = np.sqrt(12.0 * eps) * (((b - a) * sec_dev_max(f, a, b))**(-1/2.0))
    
    h = np.sqrt(12.0 * eps) / np.sqrt((b - a) * sec_dev_max(f, a, b))
    n = (b - a) / float(h)
    return (trapezint(f, a, b, n), n)

def trapezint(f, a, b, n):
    """
    Uses trapezoid rule to find the integral of a function
    """
    sum = 0.0
    h = (b - a) / float(n)
    for counter in range(int(n)):
        sum += (1 / 2.0) * h * (f(a + counter * h) + f (a + (counter + 1) * (h)))
    return sum

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def integrals():
    """
    Outputs the results of estimation of integral by the trapezoid rule for
    the given functions and outputs the errors from the actual integrals.
    """
    cos1 = adaptive_trapezint(cos, 0, np.pi)
    sin1 = adaptive_trapezint(sin, 0, np.pi)
    sin2 = adaptive_trapezint(sin, 0, np.pi / 2)
    
    exactcos = 0
    exactsin = 2
    exactsin2 = 1
    
    errorcos = abs(cos1[0] - exactcos)
    errorsin = abs(sin1[0] - exactsin)
    errorsin2 = abs(sin2[0] - exactsin2)
    
    print("Function\tError\t\t\tEstimated n")
    print("Cos [0, pi]\t" + str(errorcos) + "\t" +str(cos1[1]))
    print("Sin [0, pi]\t" + str(errorsin) + "\t" +str(sin1[1]))
    print("Sin [0, pi/2]\t" + str(errorsin2) + "\t" +str(sin2[1]))

def f(x):
    return 2 * x + 4

def test():
    print(abs(trapezint(f, 0, 2, 10)))
    assert (abs(trapezint(f, 0, 2, 10) - 12.0) < 1E-5)
    
integrals()
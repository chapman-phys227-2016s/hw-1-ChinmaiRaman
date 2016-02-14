#! /usr/bin/env python

"""
File: sinesum1.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 1.2
Date: Feb 12, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Approximates a piecewise constant function by a sum of sines
"""
import numpy as np

def S(t, n, T):
    """
    Outputs the sum of sines.
    """
    sum = 0.0
    i = 1
    while i <= n:
        sum += (1 / (2.0 * i - 1)) * np.sin((2 * np.pi * t * (2.0 * i - 1)) / T)
        i += 1
    value = (4.0 / np.pi) * sum
    return value

def f(t, T):
    """
    Outputs the results of a piecewise constant function.
    """
    if ((t > 0) and t < (T / 2)):
        return 1
    elif (abs((T / 2) - t) < 1e-14):
        return 0
    elif ((t > (T /2)) and (t < T)):
        return -1
    else:
        return None
    
listn = [1, 3, 5, 10, 30, 100]

listalpha = [0.01, 0.25, 0.49]

def output():
    """
    Tabulates information showing how the error varies with n and t for specific cases.
    """
    print("Alpha\tn\tf(t)\t\tS(t)\t\terror")
    for alpha in listalpha:
        for n in listn:
            value = f(alpha * 2.0 * np.pi, 2 * np.pi)
            value2 = S(alpha * 2.0 * np.pi, n, 2 * np.pi)
            error = value - value2
            print('%5.2f %5d %15.10f %15.10f %15.10f' % (alpha, n, value, value2, error))
            
def test():
    assert(abs(f(0.49, 2 * np.pi) - S(0.49, 1e6, 2 * np.pi)) < 1e-6), "Failure."
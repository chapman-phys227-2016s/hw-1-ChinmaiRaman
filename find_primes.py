#! /usr/bin/env python

"""
File: find_primes.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 1.4
Date: Feb 12, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: The Sieve of Eratosthenes. Finds all prime numbers less than or equal to a given number N.
"""

import numpy as np

primes = []

def sieve(N):
    """
    Finds all prime numbers less than or equal to a given number N.
    """
    for i in range(2, N + 1):
        primes.append(i)
    p = 2
    while (p < N):
        i = 2
        while((p * i) < (N + 1)):
            if ((p * i in primes) == True):
                del primes[primes.index(p * i)]
            i += 1
        p += 1

def test():
    sieve(10)
    assert([2, 3, 5, 7] == primes), "Failure."
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import math

maxPrime = 200000
primeToFind = 10001
x = [True for i in range(maxPrime)]
x[0] = x[1] = False  # manually set 0 and 1 to not be primes
for i in range(2, int(math.sqrt(maxPrime))):
    if x[i]:
        for j in range(i, math.ceil(maxPrime / i)):
            x[i * j] = False
primesFound = 0
for i in range(maxPrime):
    if x[i]:
        primesFound += 1
        # print(i)
        if primesFound == primeToFind:
            print(i)  # should be: 104743
            break

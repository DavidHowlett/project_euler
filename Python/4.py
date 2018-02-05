"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

biggest = 0
for j in range(100, 1000):
    for i in range(100, j+1):
        product = i*j
        if product > biggest and str(product)[::-1] == str(product):
                biggest = product
print(biggest)

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import primeTools

print(sum(primeTools.primes_less_then(2000000)))
# should be 142913828922

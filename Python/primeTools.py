import itertools
import math
from typing import List

known_primes: List[int] = [2]


# for other problems I want to get an iterator that gives all the primes less then x
def primes_less_then(top):
    """using sieve of Eratosthenes"""
    global known_primes
    is_a_prime = [True] * top
    is_a_prime[0] = is_a_prime[1] = False  # manually set 0 and 1 to not be primes
    for i in range(2, int(math.sqrt(top)) + 1):
        if is_a_prime[i]:
            for j in range(i, math.ceil(top / i)):
                is_a_prime[i * j] = False
    local_primes = [number for number in range(top) if is_a_prime[number]]
    if local_primes[-1] > known_primes[-1]:
        known_primes = local_primes
    return known_primes


def primes():
    """prime generator"""
    for prime in known_primes:
        yield prime
    for i in itertools.count(prime):
        for prime in known_primes:
            if i % prime == 0:
                break
            if prime * prime > i:
                known_primes.append(i)
                yield i
                break


def prime_no(x):
    """finds the xth prime, has not been optimised much"""
    try:
        return known_primes[x + 1]
    except IndexError:
        pass
    prime_generator = primes()
    for _ in range(x):
        tmp = prime_generator.__next__()
    return tmp


def prime_factors_of(x):
    prime_factors = []
    for prime in primes():
        occurrences = 0
        while x % prime == 0:
            x //= prime
            occurrences += 1
        if occurrences:
            prime_factors.append((prime, occurrences))
        if x == 1:
            return prime_factors


def num_divisors_of(x):
    prime_factors = prime_factors_of(x)
    result = 1
    for prime in prime_factors:
        result *= prime[1] + 1
    return result


if __name__ == '__main__':
    triNum = [1, 3, 6, 10, 15, 21, 28]
    for i in triNum:
        print(prime_factors_of(i))
        print(num_divisors_of(i))

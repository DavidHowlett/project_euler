import itertools
import math
# for other problems I want to get an itterator that gives all the primes less then x

knownPrimes = [2]

def primesLessThen(top):
    'useing sieve of Eratosthenes'
    global knownPrimes
    isAPrime=[True for i in range(top)]
    isAPrime[0]=isAPrime[1]=False # manually set 0 and 1 to not be primes
    for i in range(2,int(math.sqrt(top))+1):
        if isAPrime[i]:
            for j in range(i,math.ceil(top/i)):
                isAPrime[i*j]=False
    localPrimes = [number for number in range(top) if isAPrime[number]]
    if localPrimes[-1]>knownPrimes[-1]:
        knownPrimes = localPrimes
    return knownPrimes

def primes():
    'prime generator'
    for prime in knownPrimes:
        yield prime
    for i in itertools.count(prime):
        for prime in knownPrimes:
            if i%prime == 0:
                break
            if prime*prime > i:
                knownPrimes.append(i)
                yield i
                break

def prime(x):
    'finds the xth prime'
    'not optimised much'
    try:
        return knownPrimes[x+1]
    except IndexError:
        pass
    primeGenerator = primes()
    for i in range (x):
        tmp = primeGenerator.__next__()
    return tmp

def primeFactorsOf(x):
    primeFactors = []
    for prime in primes():
        occurrences = 0
        while x%prime==0:
            x//=prime
            occurrences+=1
        if occurrences:
            primeFactors.append((prime,occurrences))
        if x==1:
            return primeFactors
        
def numDivisorsOf(x):
    primeFactors = primeFactorsOf(x)
    result = 1
    for prime in primeFactors:
        result*=prime[1]+1
    return result

if __name__ == '__main__':
    triNum = [1,3,6,10,15,21,28]
    for i in triNum:    
        print(primeFactorsOf(i))
        print(numDivisorsOf(i))
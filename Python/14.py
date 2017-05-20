'''
The following iterative sequence is defined for the set of positive integers:

n to n/2 (n is even)
n to 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 to 40 to 20 to 10 to 5 to 16 to 8 to 4 to 2 to 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

preCalc = {0: 0, 1: 0}

def collatz(x):
    if x not in preCalc:
        if x%2:
            preCalc[x] = 1+collatz(x*3+1)
        else:
            preCalc[x] = 1+collatz(x//2)
    return preCalc[x]

record = 1,0
for i in range(1,1000000):
    if collatz(i)>record[1]:
        record = i,collatz(i)
print(record[0])
# took 55.4414356382241 seconds with brute force
# took 1.976053 seconds with dynamic programmigng

            

/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
*/

#include <math.h>
#include <stdio.h>
const int maxPrime = 200000;
int primesToFind=10001;
char x[maxPrime];
int i;
int main() {
    // This is an implementation of the Sieve of Eratosthenes
    // I initially set all the numbers to be possibly prime
	for(i=2;i<maxPrime;i++)
		x[i]=1;

	for(i=2;primesToFind;){
		if(x[++i]){
			for(int j=2*i;j<maxPrime;j+=i)
				x[j]=0;
            primesToFind--;
        }
    }
	printf("%d\n",i);	// should be: 104743
}

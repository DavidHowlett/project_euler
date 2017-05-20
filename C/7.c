#include <math.h>
#include <stdio.h>
const int maxPrime = 200000;
int primeToFind=10001;
char x[maxPrime];
int i=0;
int main()
{
	for(int i=0;i<maxPrime;i++)
		x[i]=1;
	x[0]=x[1]=0;// this manually sets 0 and 1 to be not prime
	for(int i=2;i<1+sqrt(maxPrime);i++)
		if(x[i])
			for(int j=2*i;j<maxPrime;j+=i)
				x[j]=0;
	int primeCount=0;
	for(i=0;i<maxPrime&&primeCount<primeToFind;)
		if(x[++i])
			primeCount++;
	printf("%d\n",i);	// should be: 104743
}

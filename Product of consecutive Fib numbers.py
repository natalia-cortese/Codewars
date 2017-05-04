"""
Challenge:

The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

"""

import math

def generateFibSequence(endPoint): #Generate the fib sequence
	sequence=[0,1]
	i=0
	while sequence[-1]<endPoint:
		sequence.append(sequence[i]+sequence[i+1])
		i+=1
	return sequence



def productFib(prod):
	prodOver2=math.floor(prod/2)
	pairIndex=0
	fib=generateFibSequence(prod)
	productFound=False
	for i in range(0,len(fib)-1):
		pairIndex=i
		currentProduct=fib[i]*fib[i+1]

		if currentProduct==prod:
			productFound=True
			break
		elif currentProduct>prod:
			break


	return [fib[pairIndex],fib[pairIndex+1],productFound]

#print(productFib(4895))
#print(productFib(5895))


""" Refined version: 

def productFib(prod):
	a,b=0,1

	while prod>a*b:
		temp=a
		a=b
		b=b+temp

	return [a,b, prod==a*b]
	
"""
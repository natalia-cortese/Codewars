"""
Challenge: Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n. 

I.e. is there an integer k such as : 
(a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
"""

def dig_pow(n, p): 
	digits=str(n)
	sum=0
	for i, digit in enumerate(digits):
		sum+=pow(int(digit),i+p) #Build sum
	if sum%n==0:  		#If sum is divisible by n,
		return sum/n    #then return k
	else:
		return -1	#Else, return -1
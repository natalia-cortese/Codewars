""" 
Challenge: You need to create a fibonacci function that given 
a signature array/list, returns the first n elements 
- signature included of the so seeded sequence.
"""
def tribonacci(signature,n):
    sequence=signature #Begin with signature (first 3 elmts)
    for i in range(2,n-1):
    	sequence.append(sequence[i-2]+sequence[i-1]+sequence[i])
    return sequence[0:n]
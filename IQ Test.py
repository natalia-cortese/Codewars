"""
Challenge: Bob is preparing to pass IQ test. 
The most frequent task in this test is to find out which one of 
the given numbers differs from the others. Bob observed that one 
number usually differs from the others in evenness. Help Bob — 
to check his answers, he needs a program that among the given 
numbers finds one that is different in evenness, and return a 
position of this number.
"""

def iq_test(numbers):

	numbers=[int(i)%2 for i in numbers.split()] #Convert to integer list indicating odd or even
	if numbers.count(1)>numbers.count(0):
		return numbers.index(0)+1
	else:
		return numbers.index(1)+1
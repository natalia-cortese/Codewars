"""
Challenge: You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.
"""

def find_outlier(integers):
	odd=[]
	even=[]
	for number in integers:
		if number%2==0:
			even.append(number)
		else:
			odd.append(number)
	if len(even)==1:
		return even[0]
	else:
		return odd[0]

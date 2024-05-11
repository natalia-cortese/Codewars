"""
Challenge: Given a list of integers and a single sum value, 
return the first two values (parse from the left please) 
in order of appearance that add up to form the sum.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. 
Be sure your code doesn't time out.

Reader-note: This algorithm was created after observing others' much simpler solutions.
"""

def sum_pairs(ints, s):
	seen=set()
	for num in ints:
		if s-num in seen:
			return [s-num, num]
		seen.add(num)
	

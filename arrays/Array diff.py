"""
Challenge: Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list a, which are present in list b.
"""
def array_diff(a, b):
    for num in b:
    	if num in a:
    		a=[x for x in a if x!=num]
    return a
"""
Challenge:
Given a two-dimensional array of integers, 
return the flattened version of the array with 
all the integers in the sorted (ascending) order.
"""

def flatten_and_sort(array):
	newArray=[]
	for subArray in array:
		for x in subArray:
			newArray.append(x)
	return sorted(newArray)

"""
Refined solution
"""
def flatten_and_sort2(array):
	newArray=[x for subArray in array for x in subArray]
	return sorted(newArray)
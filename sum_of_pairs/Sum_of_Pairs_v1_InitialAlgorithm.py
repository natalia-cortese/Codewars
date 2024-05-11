"""
Challenge: Given a list of integers and a single sum value, 
return the first two values (parse from the left please) 
in order of appearance that add up to form the sum.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. 
Be sure your code doesn't time out.

Self-note: This version is too complex for larger lists.
"""

def findSmallestPair(iPairs):
	smallestPair=iPairs[0]
	for pair in iPairs:
		if pair!=smallestPair:
			if smallestPair[1]>pair[1]: #If second element is larger, pair is new smallest
				smallestPair=pair
	return smallestPair


def sum_pairs(ints, s):
	indexPairs=[]

	for i in range(0,len(ints)):	#Add all index pairs whose elements add up to s
		for j in range(i+1,len(ints)):
			if s==ints[i]+ints[j]:
				indexPairs.append([i,j])
				break #Exit when first pair is found

	if indexPairs:
		index1,index2=findSmallestPair(indexPairs)#Find smallest pair
		return [ints[index1],ints[index2]]
"""
Challenge: Given a list of integers and a single sum value, 
return the first two values (parse from the left please) 
in order of appearance that add up to form the sum.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. 
Be sure your code doesn't time out.

Self-note: This algorithm cannot be O(n^2) complexity
"""

## A function to find the smallest pair of indexes ##
def findSmallestPair(pairs):
	smallestPair=pairs[0]
	for pair in pairs:
		if smallestPair[1]>pair[1] and pair[0]>-1: #If second element is larger, pair is new smallest
			smallestPair=pair
	return smallestPair


## A function to find an index pair for any given number ##
def findIndexPairForNumber(num,sumList,ints,s):
	index1=sumList.index(num)
	index2=-1
	for i in range(0,len(ints)):	#Add all index pairs whose elements add up to s
		if ints[i]==s-ints[index1] and i!=index1:
			index2=i
			
	if index1>index2:
		return [index2,index1] #Add each potential index
	else:
		return [index1,index2] #Add each potential index


## Main function to find the first pair which sums to s ##
def sum_pairs(ints, s):
	
	sumList=[s-x for x in ints]
	sumSet=list(set(sumList))    #Remove duplicates

	indexPairs=[]

	for num in sumSet:   #Find pair for each unique num
		if num in ints:
			newIndexPair=findIndexPairForNumber(num,sumList,ints,s)
			indexPairs.append(newIndexPair)

	if indexPairs:
		index1,index2=findSmallestPair(indexPairs)
		return [ints[index1],ints[index2]]



#l1= [1, 4, 8, 7, 3, 15]
#l2= [10, 5, 2, 3, 7, 5]

#print(sum_pairs(l1, 4))
#print(sum_pairs(l2, 10))
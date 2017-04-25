"""
Challenge: Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1). 
"""

#The solution can also be obtained by the mathematical insight which reveals the sum to be n**3.

def starting(i):  #Calculate first number of row recursively
	if i==1:
		return 1
	return starting(i-1)+(i-1)*2


def row_sum_odd_numbers(n):
    firstNumberInRow=starting(n) 	#Initalize the first number in the row
    rowSum=0  						#Initialize the rowSum

    for i in range(0,n):			#Add element for each number in row
    	rowSum+=firstNumberInRow+2*i

    return rowSum


"""
Challenge: Your task is to make a function that can take any non-negative integer 
as a argument and return it with it's digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
"""

def Descending_Order(num):
	reversedNum=''.join(sorted(str(num), reverse=True))
	return int(reversedNum)

solution = Descending_Order(12839171946124)
print(solution)

solution2 = Descending_Order(1112222333)
print(solution2)
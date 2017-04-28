"""
Challenge: You need to create a function that will validate if given parameters are valid geographical coordinates.

Valid coordinates look like the following: "23.32353342, -32.543534534". The return value should be either true or false.

Latitude (which is first float) can be between 0 and 90, positive or negative. Longitude (which is second float) can be between 0 and 180, positive or negative.

Coordinates can only contain digits, or one of the following symbols (including space after comma) -, .

There should be no space between the minus "-" sign and the digit after it.
"""

def hasNonNumericCharacters(coordinate):
	nonNumeric=[x for x in coordinate if x.isdigit()==False]
	if nonNumeric:
		if nonNumeric==['-'] and coordinate[0]=='-' and len(coordinate)>1:
			print("Acceptable non-numeric characters")
		elif nonNumeric==['-','.'] and coordinate[0]=='-'and len(coordinate)>2:
			print("Acceptable non-numeric characters")
		elif nonNumeric==['.'] and len(coordinate)>1:
			print("Acceptable non-numeric characters")
		else:
			return True
	return False


def convertInput(coordinates):
	coordinates=coordinates.split() #Split the numbers
	if len(coordinates)!=2:  		#Return invalid co-ordinates if invalid input
		return ['not','valid']
	coordinates[0]=coordinates[0][:-1]    #Remove the comma
	return coordinates


def is_valid_coordinates(coordinates):
	latitude,longitude=convertInput(coordinates)
	if hasNonNumericCharacters(latitude) or hasNonNumericCharacters(longitude): #non-numeric
		print('Returned false for non-numeric')
		return False
	elif abs(float(latitude))>90 or abs(float(longitude))>180: #Out of range
		print('Returned false for range')
		return False

	print("Valid Co-ordinates")
	return True 

	
#E.g. print(is_valid_coordinates("-23, 25"))
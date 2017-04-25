"""
Challenge: Create function which transforms letters according to patter.
"""

def accum(s):
    mumble=s[0].upper()  #Add the first element (1 uppercase letter)
    letterLocation=2
    for letter in s[1:]:
	    mumble+="-"+letter.upper()  #Add the dash and initial upper-case character
	    lower=letter.lower()
	    for location in range(1,letterLocation):	#Add specified number of lowercase letters
		    mumble+=lower
	    letterLocation+=1
    return mumble
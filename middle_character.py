"""
Challenge:
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

Note: completed in python 2 as per challenge requirements. This will not properly function in python 3 due to the way division works.
"""

def get_middle(s):
    half=len(s)/2
    return s[half] if len(s)%2==1 else s[half-1:half+1]




"""
#Original solution:
def get_middle(s):
    half=len(s)/2
    if len(s)%2==1:
        return s[half]
    else:
        return s[half-1:half+1]
 """
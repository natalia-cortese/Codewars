"""
Challenge: Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.
"""
def getCount(inputStr):    
    return len([x for x in list(inputStr) if x in list('aeiouAEIOU')])
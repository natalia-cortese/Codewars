"""
Instructions:
Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.

You have to validate input:

-v can be anything (primitive or otherwise)
-if v is ommited, fill the array with undefined
-if n is 0, return an empty array
-if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.
"""

#Reworked solution without loop

def prefill(n=0, v=None):    
    try:
        return [v]*int(n)
    except:
        raise TypeError(str(n) + " is invalid")


""" 
#Original solution

def prefill(*args):
    outArray=[]
    try:                    # Check for proper arguments
        n,v = args 
        try:                    #Check for valid n
            n=int(n)
            try:                #If no v provided, add undefined elements
                element=v
            except: 
                element=""
                
            for i in range(0,n):
                outArray.append(element)
            return outArray
            
        except ValueError:
            print(str(n)+ " is invalid.")
        except TypeError:
            print(str(n)+ " is invalid.")
    except:
        return []
  """  
        
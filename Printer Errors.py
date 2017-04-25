"""Challenge: You have to write a function printer_error
which given a string will output the error rate
of the printer as a string representing a rational
whose numerator is the number of errors and the denominator
the length of the control string."""

def printer_error(s):
    goodLetters='abcdefghijklm'

    errors=0
    totalLetters=len(s)

    for letter in s:
        if letter not in goodLetters:
            errors+=1

    return str(errors) + "/" + str(totalLetters)

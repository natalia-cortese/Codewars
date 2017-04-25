def printer_error(s):
    goodLetters='abcdefghijklm'

    errors=0
    totalLetters=len(s)

    for letter in s:
        if letter not in goodLetters:
            errors+=1

    return str(errors) + "/" + str(totalLetters)

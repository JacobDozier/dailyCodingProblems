import string

def getAlphaMap():
    dictionary = {}
    for position in range(26):
        dictionary.update(dict.fromkeys(string.ascii_lowercase[position], position))
    
    for key in dictionary.keys():
        dictionary[key] = str(dictionary.get(key) + 1)

    return dictionary

def findCharsInInput(passedAlphaMap, passedInput):
    foundChars = {}
    for key, value in passedAlphaMap.items():
        if value in passedInput:
            foundChars.update(((key, value),))
    return foundChars


if __name__ == "__main__":
    userInput = '1213'
    userInputCopy = userInput
    numSolutions = 0
    alphaMap = getAlphaMap()

    foundChars = findCharsInInput(alphaMap, userInput)
    print('sorted foundChars:', foundChars)
    print('foundChars length:', str(len(foundChars)))

    print('numSolutions:', numSolutions)
    print('done')

import string

def getAlphaMap():
    dictionary = {}
    for position in range(26):
        dictionary.update(dict.fromkeys(string.ascii_lowercase[position], position))
    
    for key in dictionary.keys():
        dictionary[key] = dictionary.get(key) + 1

    return dictionary

if __name__ == "__main__":
    alphaMap = getAlphaMap()
    # TODO implement
    print("Work in progress")
    print(alphaMap)
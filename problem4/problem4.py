arr = [-1, 0, -4, 2, 4, 0, 1]
negArr = []

def separateNegatives(arrIn):
    newArr = []
    negatvieArr = []
    for number in arrIn:
        if number >= 0:
            newArr.append(number)
        else:
            negatvieArr.append(number)
    return newArr, negatvieArr

def findMissingNumber(sortedList):
    prevNum = arr[0]
    foundValue = 0
    for value in sortedList:
        if (value - prevNum) > 1:
            foundValue = (prevNum + 1)
            break
        elif 1 not in arr:
            foundValue = 1
            break
        else:
            foundValue = value + 1
        prevNum = value
    return foundValue

if __name__ == '__main__':

    arr, negArr = separateNegatives(arr)
    arr.sort()
    missingNo = findMissingNumber(arr)

    print(str(negArr + arr))
    print(missingNo)

arr = [-1, 0, -4, 1, 4, 2]
missingNo = 0

arr.sort()

def separateNegatives(arr):
    newArr = []
    negatvieArr = []
    for number in arr:
        if number >= 0:
            newArr.append(number)
        else:
            negatvieArr.append(number)
    return newArr, negatvieArr
            

arr, negArr = separateNegatives(arr)

# TODO Is the lowest value necessary?
lowestValue = arr[-1]
for number in arr:
    if number > 0 and number < lowestValue:
        lowestValue = number

print(lowestValue)

prevNum = arr[0]
for value in arr:
    if (value - prevNum) > 1 and prevNum == lowestValue:
        missingNo = (lowestValue + 1)
        break
    # TODO This will always satisfy if 1 is in the list and exit the loop.
    elif (value - prevNum) == 1 and prevNum == lowestValue:
        missingNo = 1
        break
    else:
        missingNo = value + 1
    prevNum = value

print(str(negArr + arr))
print(missingNo)
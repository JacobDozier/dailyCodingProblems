arr = [-1, 0, 3, -4, 4, 2]
missingNo = 0

arr.sort()

def clearNegatives(arr):
    newArr = []
    for number in arr:
        if number >= 0:
            newArr.append(number)
    return newArr
            

arr = clearNegatives(arr)
lowestValue = arr[-1]

for number in arr:
    if number > 0 and number < lowestValue:
        lowestValue = number

prevNum = arr[0]
for value in arr:
    if arr.index(value) != 0:
        if (value - prevNum) > 1 and prevNum == lowestValue:
            missingNo = (lowestValue + 1)
            break
        else:
            missingNo = value + 1
    prevNum = value

print(arr)
print(missingNo)
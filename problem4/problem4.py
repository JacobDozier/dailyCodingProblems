arr = [-1, 0, -4, 3, 4, 0, 1]
negArr = []
missingNo = 0

def separateNegatives(arrIn):
    newArr = []
    negatvieArr = []
    for number in arrIn:
        if number >= 0:
            newArr.append(number)
        else:
            negatvieArr.append(number)
    return newArr, negatvieArr
            

arr, negArr = separateNegatives(arr)
arr.sort()

prevNum = arr[0]
for value in arr:
    if (value - prevNum) > 1:
        missingNo = (prevNum + 1)
        break
    elif 1 not in arr:
        missingNo = 1
        break
    else:
        missingNo = value + 1
    prevNum = value

print(str(negArr + arr))
print(missingNo)
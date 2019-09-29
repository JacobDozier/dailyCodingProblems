inputArray = [1, 2, 3, 4, 5]
outputArray = []

for index, item in enumerate(inputArray):
    arrayProduct = 1
    for jIndex, jItem in enumerate(inputArray):
        if jIndex != index:
            arrayProduct = arrayProduct * jItem
    outputArray.append(arrayProduct)

print(outputArray)
numbers = [10, 15, 3, 7]

k = 17

print("starting...");

for number in numbers:
	for secondNumber in numbers:
		if number + secondNumber == 17:
			print("True " + str(number) + " + " + str(secondNumber) + " = " + str(k));
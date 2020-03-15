cents = 133
originalCents = cents
productOfCoins = 0
numCoins = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
counter = 0

# Need to start with the larges coin (25c) and work my way down.
# Divide cents by coin size to determine how many should be in there.
# Take the remainder and use that for the next size down.
# In this example it would be 0 quarters 1 dime 1 nickel 1 penny. numCoins = 3.

print("cents: " + str(cents))

while(productOfCoins != originalCents):
    if(cents > 25):
        quarters = cents // 25
        cents -= quarters * 25
        numCoins += quarters
        productOfCoins += quarters * 25
        print("quarters: " + str(quarters))
    elif(cents > 10):
        dimes = cents // 10
        cents -= dimes * 10
        numCoins += dimes
        productOfCoins += dimes * 10
        print("dimes: " + str(dimes))
    elif(cents > 5):
        nickels = cents // 5
        cents -= nickels * 5
        numCoins += nickels
        productOfCoins += nickels * 5
        print("nickels: " + str(nickels))
    else:
        pennies = cents
        numCoins += pennies
        productOfCoins += pennies
        print("pennies: " + str(pennies))

print("numCoins: " + str(numCoins))
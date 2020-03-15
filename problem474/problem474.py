cents = 133
originalCents = cents
productOfCoins = 0
numCoins = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
counter = 0

print("cents: " + str(cents))

if(cents > 25):
    quarters = cents // 25
    cents -= quarters * 25
    numCoins += quarters
    productOfCoins += quarters * 25
    print("quarters: " + str(quarters))
if(cents > 10):
    dimes = cents // 10
    cents -= dimes * 10
    numCoins += dimes
    productOfCoins += dimes * 10
    print("dimes: " + str(dimes))
if(cents > 5):
    nickels = cents // 5
    cents -= nickels * 5
    numCoins += nickels
    productOfCoins += nickels * 5
    print("nickels: " + str(nickels))

pennies = cents
numCoins += pennies
productOfCoins += pennies
print("pennies: " + str(pennies))

print("numCoins: " + str(numCoins))
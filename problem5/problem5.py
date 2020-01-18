def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def getPair(a, b):
    fTuple = (a, b)
    return fTuple

def car(f):
    firstValue = f(getPair)
    return firstValue[0]

def cdr(f):
    lastValue = f(getPair)
    return lastValue[-1]

if __name__ == "__main__":
    print("Pair: (3, 4)")
    print("car: " + str(car(cons(3, 4))))
    print("cdr: " + str(cdr(cons(3, 4))))

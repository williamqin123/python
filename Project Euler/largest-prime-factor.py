import time
lastRecordedTime = 0
factors = [[0, [0]]]
primeFactors = []
factorsList = None
epochTime = None
def getTime():
    global epochTime
    epochTime = time.time()# * 10
    return epochTime
def reset():
    global factorsList
    factorsList = factors[len(factors)-1]
def record():
    reset()
    if len(factorsList[1]) == 2:
        prime = factorsList[0]
        try:
            primeFactors.index(prime)
        except Exception:
            primeFactors.append(prime)
            pass
def scan(number, recursive):
    global lastRecordedTime
    for factor in range(1, number+1):
        if number % factor == 0:
            if not recursive:
                reset()
                factorsList[1].append(factor)
                continue
            else:
                factors.append([factor, []])
                scan(factor, recursive=False)
        if recursive:
            record()
        getTime()
        if epochTime - lastRecordedTime >= 1:
            print(chr(27) + "[2J")
            print("Calculating iteration number %d out of %d." % (factor, number))
            elapsed = (epochTime - startTime) / 10
            calcTime = int(elapsed * (number / factor) - elapsed)
            print(elapsed)
            print(number / factor)
            print(calcTime)
            minutes = int(calcTime/60)
            hours = int(minutes/60)
            print("The estimated time left to compute is (%d) hours, (%d) minutes, and (%d) seconds." % (hours, minutes - hours * 60, calcTime - minutes * 60))
            lastRecordedTime = epochTime
startTime = getTime()
scan(600851475143, recursive=True)
print("\n\nThe prime factors of 600851475143 are %s." % str(primeFactors))
print("The greatest prime factor of 600851475143 is %d." % list(reversed(primeFactors))[0])
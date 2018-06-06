primes=[2] # 1st prime

def findNextPrime():
	lastPrime = primes[len(primes) - 1]
	while True:
		lastPrime += 1
		for i in primes:
			if lastPrime % i == 0:
				break
			if i * i > lastPrime:
				primes.append(lastPrime)
				return

def findPrimes(until):
	for i in range(0, until):
		findNextPrime()

findPrimes(10000) # 1st prime is already found
print(primes)
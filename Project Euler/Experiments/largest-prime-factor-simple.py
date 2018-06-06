primeFactors = []
number = 600851475143
counter = 0
iterationRecord = 0
for i in range(1, number+1):
    if i - iterationRecord >= counter:
        print(chr(27) + "[2J")
        print("The calculations have progressed by %s percent." % str(i / number * 100)[0:5])
        print("This is loop iteration number %d out of %d." % (i, number))
        counter = 123451
        iterationRecord = i
    if not number % i == 0:
        continue
    factors = 0
    for x in range(1, i+1):
        if i % x == 0:
            factors += 1
    if factors <= 2:
        primeFactors.append(i)
        print("The prime factor %d has been detected!" % i)
        counter = 10000000
print("The prime factors of %d are %s!" % (number, str(primeFactors)))
print("The greatest prime factor of %d is %d!" % (number, list(reversed(primeFactors))[0]))
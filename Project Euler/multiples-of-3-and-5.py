sum = 0
for x in range(0, 1000):
    if x % 3 == 0 or x % 5 == 0:
        print("%d is a multiple of 3 or 5." % x)
        sum += x
print("The sum of all the multiples of 3 or 5 that are below 1000 is %d." % sum)
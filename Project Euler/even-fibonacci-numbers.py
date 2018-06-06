x = 2
y = 1
z = 0
while x < 4000000:
    if x % 2 == 0:
        print("%d is an even Fibonacci number." % x)
        z += x
    i = x
    x += y
    y = i
print("The sum of all the even Fibonacci numbers that are below 4 million is %d." % z)